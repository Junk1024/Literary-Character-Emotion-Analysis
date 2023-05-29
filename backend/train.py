import numpy as np
import os
from paddlenlp.transformers import LinearDecayWithWarmup
from functools import partial
import paddle
import pandas as pd
import paddle.nn.functional as F
import paddlenlp as ppnlp
import matplotlib
import matplotlib.pyplot as plt
from paddlenlp.data import Pad, Stack, Tuple
from paddlenlp.datasets import DatasetBuilder


train = pd.read_csv('./data/usual_train.csv')  # 通用训练数据集
eval = pd.read_csv('./data/usual_eval_labeled.csv')   # 通用验证数据集
test = pd.read_csv('./data/usual_test_labeled.csv') # 通用测试数据集
total = pd.concat([train,eval,test])  # 构造总数据集便于统计分析

train['label'] = train['情绪标签']
eval['label'] = eval['情绪标签']
test['label'] = test['情绪标签']
total['label'] = total['情绪标签']

train['text_a'] = train['文本']
eval['text_a'] = eval['文本']
test['text_a'] = test['文本']
total['text_a'] = total['文本']

train = train[['text_a', 'label']]
eval = eval[['text_a', 'label']]
test = test[['text_a', 'label']]
total = total[['text_a', 'label']]

# 查看数据前5条
print(total.head())
# 查看总数据文件信息,可以看出共计有48374条数据
print(total.info())
# 查看训练数据文件信息
print(train.info())
#text_a文本列是存在缺失值的，直接清除缺失值所在行
train = train.dropna(subset=['text_a'])
total = total.dropna(subset=['text_a'])
# 统计文本长度，便于确定文本最大截断长度
print(total['text_a'].map(len).describe())
# 统计数据集中类别标签的分布情况
print(total['label'].value_counts())
print('xunlian:',train['label'].value_counts())
print('xunlian:',eval['label'].value_counts())
print('xunlian:',test['label'].value_counts())
# 定义要进行分类的类别
label_list=list(train.label.unique())
print(label_list)
total['label'].value_counts(normalize=True).plot(kind='bar')
plt.show()
model = ppnlp.transformers.NeZhaForSequenceClassification.from_pretrained('nezha-large-wwm-chinese', num_classes=6)
tokenizer =  ppnlp.transformers.NeZhaTokenizer.from_pretrained('nezha-large-wwm-chinese')

# 定义数据集对应文件及其文件存储格式
class EmotionData(DatasetBuilder):
    SPLITS = {
        'train': 'train.csv',  # 训练集
        'dev': 'valid.csv',    # 验证集
        'test': 'test.csv',    # 测试集
    }

    def _get_data(self, mode, **kwargs):
        filename = self.SPLITS[mode]
        return filename

    def _read(self, filename):
        """读取数据"""
        with open(filename, 'r', encoding='utf-8') as f:
            head = None
            for line in f:
                data = line.strip().split("\t")    # 以'\t'分隔各列
                if not head:
                    head = data
                else:
                    text_a, label = data
                    yield {"text_a": text_a, "label": label}  # 数据的格式：text_a,label

    def get_labels(self):
        return label_list   # 类别标签

# 定义数据集加载函数
def load_dataset(name=None,
                 data_files=None,
                 splits=None,
                 lazy=None,
                 **kwargs):

    reader_cls = EmotionData
    print(reader_cls)
    if not name:
        reader_instance = reader_cls(lazy=lazy, **kwargs)
    else:
        reader_instance = reader_cls(lazy=lazy, name=name, **kwargs)

    datasets = reader_instance.read_datasets(data_files=data_files, splits=splits)
    return datasets

# 加载训练、验证集和测试集
train_ds, dev_ds, test_ds = load_dataset(splits=["train", "dev", "test"])

# 定义数据加载和处理函数
def convert_example(example, tokenizer, max_seq_length=512, is_test=False):
    qtconcat = example["text_a"]
    encoded_inputs = tokenizer(text=qtconcat, max_seq_len=max_seq_length)
    input_ids = encoded_inputs["input_ids"]
    token_type_ids = encoded_inputs["token_type_ids"]

    if not is_test:
        label = np.array([example["label"]], dtype="int64")
        return input_ids, token_type_ids, label
    else:
        return input_ids, token_type_ids

# 数据加载函数dataloader
def create_dataloader(dataset,
                      mode='train',
                      batch_size=1,
                      batchify_fn=None,
                      trans_fn=None):
    if trans_fn:
        dataset = dataset.map(trans_fn)

    shuffle = True if mode == 'train' else False
    if mode == 'train':
        batch_sampler = paddle.io.DistributedBatchSampler(
            dataset, batch_size=batch_size, shuffle=shuffle)
    else:
        batch_sampler = paddle.io.BatchSampler(
            dataset, batch_size=batch_size, shuffle=shuffle)

    return paddle.io.DataLoader(
        dataset=dataset,
        batch_sampler=batch_sampler,
        collate_fn=batchify_fn,
        return_list=True)


# 批处理大小，显存如若不足的话可以适当改小该值
batch_size = 2
# 文本序列最大截断长度，需要根据文本具体长度进行确定，不超过512
max_seq_length = 128

# 将数据处理成模型可读入的数据格式
trans_func = partial(
    convert_example,
    tokenizer=tokenizer,
    max_seq_length=max_seq_length)

batchify_fn = lambda samples, fn=Tuple(
    Pad(axis=0, pad_val=tokenizer.pad_token_id),  # input_ids
    Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # token_type_ids
    Stack()  # labels
): [data for data in fn(samples)]

# 训练集迭代器
train_data_loader = create_dataloader(
    train_ds,
    mode='train',
    batch_size=batch_size,
    batchify_fn=batchify_fn,
    trans_fn=trans_func)

# 验证集迭代器
dev_data_loader = create_dataloader(
    dev_ds,
    mode='dev',
    batch_size=batch_size,
    batchify_fn=batchify_fn,
    trans_fn=trans_func)

# 测试集迭代器
test_data_loader = create_dataloader(
    test_ds,
    mode='test',
    batch_size=batch_size,
    batchify_fn=batchify_fn,
    trans_fn=trans_func)

# 定义训练过程中的最大学习率
learning_rate = 2e-5
# 训练轮次
epochs = 4
# 学习率预热比例
warmup_proportion = 0.1
# 权重衰减系数，类似模型正则项策略，避免模型过拟合
weight_decay = 0.01

num_training_steps = len(train_data_loader) * epochs
lr_scheduler = LinearDecayWithWarmup(learning_rate, num_training_steps, warmup_proportion)

# AdamW优化器
optimizer = paddle.optimizer.AdamW(
    learning_rate=lr_scheduler,
    parameters=model.parameters(),
    weight_decay=weight_decay,
    apply_decay_param_fun=lambda x: x in [
        p.name for n, p in model.named_parameters()
        if not any(nd in n for nd in ["bias", "norm"])
    ])

criterion = paddle.nn.loss.CrossEntropyLoss()  # 交叉熵损失函数
metric = paddle.metric.Accuracy()  # accuracy评价指标

@paddle.no_grad()
def evaluate(model, criterion, metric, data_loader):
    """
    Given a dataset, it evals model and computes the metric.

    Args:
        model(obj:`paddle.nn.Layer`): A model to classify texts.
        data_loader(obj:`paddle.io.DataLoader`): The dataset loader which generates batches.
        criterion(obj:`paddle.nn.Layer`): It can compute the loss.
        metric(obj:`paddle.metric.Metric`): The evaluation metric.
    """
    model.eval()
    metric.reset()
    losses = []
    for batch in data_loader:
        input_ids, token_type_ids, labels = batch
        logits = model(input_ids, token_type_ids)
        loss = criterion(logits, labels)
        losses.append(loss.numpy())
        correct = metric.compute(logits, labels)
        metric.update(correct)
        accu = metric.accumulate()
    print("eval loss: %.5f, accu: %.5f" % (np.mean(losses), accu))
    model.train()
    metric.reset()
    return accu  # 返回准确率


save_dir = "checkpoint"
if not  os.path.exists(save_dir):
    os.makedirs(save_dir)
pre_accu=0
accu=0
global_step = 0
for epoch in range(1, epochs + 1):
    for step, batch in enumerate(train_data_loader, start=1):
        input_ids, segment_ids, labels = batch
        logits = model(input_ids, segment_ids)
        loss = criterion(logits, labels)
        probs = F.softmax(logits, axis=1)
        correct = metric.compute(probs, labels)
        metric.update(correct)
        acc = metric.accumulate()

        global_step += 1
        if global_step % 10 == 0 :
            print("global step %d, epoch: %d, batch: %d, loss: %.5f, acc: %.5f" % (global_step, epoch, step, loss, acc))
        loss.backward()
        optimizer.step()
        lr_scheduler.step()
        optimizer.clear_grad()
    # 每轮结束对验证集进行评估
    accu = evaluate(model, criterion, metric, dev_data_loader)
    print(accu)
    if accu > pre_accu:
        # 保存较上一轮效果更优的模型参数
        save_param_path = os.path.join(save_dir, 'mymodel_state.pdparams')  # 保存模型参数
        paddle.save(model.state_dict(), save_param_path)
        pre_accu=accu
tokenizer.save_pretrained(save_dir)

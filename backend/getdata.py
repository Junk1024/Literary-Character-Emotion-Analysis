from base import predict
import os
import csv
import paddle
import paddlenlp as ppnlp
label_list = ['angry', 'happy', 'neutral', 'surprise', 'sad', 'fear']
label_map = {idx: label for idx, label in enumerate(label_list)}
model = ppnlp.transformers.NeZhaForSequenceClassification.from_pretrained('nezha-large-wwm-chinese', num_classes=6)
tokenizer = ppnlp.transformers.NeZhaTokenizer.from_pretrained('nezha-large-wwm-chinese')
print(str.center("NeZha模型导入完毕",80,"="))
params_path = 'checkpoint/model_state.pdparams'
if params_path and os.path.isfile(params_path):
    # 加载模型参数
    state_dict = paddle.load(params_path)
    model.set_dict(state_dict)
    print("Loaded parameters from %s" % params_path)
    print(str.center("模型参数加载完毕",80,"="))
batch_size=1
# 指定文件夹路径
folder_path = "data/deepextract/"
# 获取文件夹下的所有文件名
file_names = os.listdir(folder_path)
# 打印所有文件名
for file_name in file_names:
    # print(file_name)
    f = open(f'roledata/{file_name}.csv', 'w', encoding='utf-8', newline="")
    #  2.基于文件对象构建csv写入对象
    csv_write = csv.writer(f)

    #  3.构建列表头
    # csv_write.writerow(['text_a', 'label'])

    #  5.关闭文件

    text= open(f'data/deepextract/{file_name}', 'r')
    for i in text:

        result=predict(model, i, tokenizer, label_map, batch_size)
        label=result[0]
        csv_write.writerow([f'{i}', f'{label}'])

    f.close()




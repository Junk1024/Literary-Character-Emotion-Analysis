from base import predict
import paddlenlp as ppnlp
import os
import paddle
from getcontent import line1
text= open(f'data/deepextract/{line1}.txt', 'r')
batch_size = 1
label_list = ['angry', 'happy', 'neutral', 'surprise', 'sad', 'fear']
label_map = {idx: label for idx, label in enumerate(label_list)}
model = ppnlp.transformers.NeZhaForSequenceClassification.from_pretrained('nezha-large-wwm-chinese', num_classes=6)
tokenizer = ppnlp.transformers.NeZhaTokenizer.from_pretrained('nezha-large-wwm-chinese')
# 导入模型权重参数
params_path = 'checkpoint/model_state.pdparams'
if params_path and os.path.isfile(params_path):
    # 加载模型参数
    state_dict = paddle.load(params_path)
    model.set_dict(state_dict)
    print("Loaded parameters from %s" % params_path)
    print(str.center("模型参数加载完毕",80,"="))

# 模型预热
batch_size = 1
input_text = "今天吃火锅，香死我了！！！"
result=predict(model, input_text, tokenizer, label_map, batch_size)
print(result)
print(result[0])
a=b=c=d=e=f=0
total=0
scoal=0
for i in text:
    result=predict(model, i, tokenizer, label_map, batch_size)
    total+=1
    if result[0] == 'angry':
        scoal+=0
    elif result[0] == 'happy':
        scoal+=1
    elif result[0] == 'neutral':
        scoal+=2
    elif result[0] == 'surprise':
        scoal+=3
    elif result[0] == 'sad':
        scoal+=4
    elif result[0] == 'fear':
        scoal+=5
last=scoal/total
print(scoal,total)
label=''
if 0<last<=1:
    label='厌世'
elif 1<last<=2:
    label='善良'
elif 2<last<=3:
    label='懦弱'
elif 3<last<=4:
    label='开朗'
elif 4<last<=5:
    label='乐观'
print(label)


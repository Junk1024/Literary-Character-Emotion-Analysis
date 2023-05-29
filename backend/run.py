# 后端运行文件
import time
import os
import paddle
from base import predict
from pydantic import BaseModel
import paddlenlp as ppnlp
from fastapi import FastAPI, HTTPException,UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from getname import getlist
from getcontent import getsentences
import pandas as pd
# 定义6个分类类别

label_list = ['angry', 'happy', 'neutral', 'surprise', 'sad', 'fear']
label_map = {idx: label for idx, label in enumerate(label_list)}

# 导入NeZha模型
model = ppnlp.transformers.NeZhaForSequenceClassification.from_pretrained('nezha-large-wwm-chinese', num_classes=6)
tokenizer = ppnlp.transformers.NeZhaTokenizer.from_pretrained('nezha-large-wwm-chinese')
print(str.center("NeZha模型导入完毕",80,"="))

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
input_text = "终于把我的工作做完了！"
predict(model, input_text, tokenizer, label_map, batch_size)
print(str.center("模型预热完毕",80,"="))
print(str.center("正在启动服务",80,"="))

# 创建 FastAPI 实例
PublicSentimentAnalysis = FastAPI()

# 设置跨域
PublicSentimentAnalysis.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 单文本情感分析接口
@PublicSentimentAnalysis.get("/singleSentimentAnalysis/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def SingleSentimentAnalysis(text: str):
    try:
        # 获取用户输入的要进行属性级情感分析的文本内容
        input_text = text
        # 调用加载好的模型进行属性级情感分析
        singleAnalysisResult = predict(model, input_text, tokenizer, label_map, batch_size)
        # 接口结果返回
        results = {"message": "success", "inputText": input_text, "singleAnalysisResult": singleAnalysisResult[0]}
        return results
    # 异常处理
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail=str("请求失败，服务器端发生异常！异常信息提示：" + str(e)))

# 文本上传人物名单获取接口
# 定义路径操作装饰器：POST方法 + API接口路径
@PublicSentimentAnalysis.post("/v1/batchEmotionAnalysis/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def BatchEmotionAnalysis(file: UploadFile):
    # 读取上传的文件
    fileBytes = file.file.read()
    fileName = file.filename
    # 判断上传文件类型
    fileType = fileName.split(".")[-1]
    if fileType != "txt" and fileType != "xlsx":
        raise HTTPException(status_code=406, detail=str("请求失败，上传文件格式不正确！请上传Excel文件！"))
    try:
        # 将添加时间标记重命名避免重复
        now_time = int(time.mktime(time.localtime(time.time())))
        global filePath
        filePath = "./data/" + str(now_time) + "_" + fileName

        # 将用户上传的文件保存到本地
        fout = open(filePath, 'wb')
        fout.write(fileBytes)
        fout.close()
        info=getlist(filePath)
        results = {"message": "success","data": info}
        return results
    # 异常处理
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail=str("请求失败，服务器端发生异常！异常信息提示：" + str(e)))

# 人物相关文本提取接口
@PublicSentimentAnalysis.get("/getcontent/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def GetContent(text: str):
    try:
        # 获取用户输入的要进行属性级情感分析的文本内容
        name = text
        # 调用加载好的模型进行属性级情感分析
        getsentences(name,filePath)
        # 接口结果返回
        results = {"message": "success", "info": "角色对应文本已提取到后台文件夹"}
        return results
    # 异常处理
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail=str("请求失败，服务器端发生异常！异常信息提示：" + str(e)))

# 人物情感分析接口
@PublicSentimentAnalysis.get("/roleanalysis/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def RoleRnalysis(name: str):
    try:
        # 获取用户输入的要进行属性级情感分析的文本内容
        text= open(f'data/deepextract/{name}.txt', 'r')
        # 调用加载好的模型进行属性级情感分析
        getsentences(name,filePath)
        total=0
        a=b=c=d=e=f=0
        scoal=0
        for i in text:
            result=predict(model, i, tokenizer, label_map, batch_size)
            total+=1
            if result[0] == 'angry':
                scoal+=0
                a+=1
            if result[0] == 'sad':
                scoal+=1
                b+=1
            if result[0] == 'fear':
                scoal+=2
                c+=1
            if result[0] == 'neutral':
                scoal+=3
                d+=1
            if result[0] == 'happy':
                scoal+=4
                e+=1
            if result[0] == 'surprise':
                scoal+=5
                f+=1
        last=scoal/total
        print(scoal,total)
        label=''
        if 0<last<=1:
            label='厌世'
        elif 1<last<=2:
            label='懦弱'
        elif 2<last<=3:
            label='善良'
        elif 3<last<=4:
            label='开朗'
        elif 4<last<=5:
            label='乐观'
        print(label)
        labellist=[{'name':'angry','value':a},
                   {'name':'sad','value':b},
                   {'name':'fear','value':c},
                   {'name':'neutral','value':d},
                   {'name':'happy','value':e},
                   {'name':'surprise','value':f}
                   ]
        # 接口结果返回
        results = {"message": "success", "label": label,"labellist": labellist}
        return results
    # 异常处理
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail=str("请求失败，服务器端发生异常！异常信息提示：" + str(e)))


uvicorn.run(PublicSentimentAnalysis, host="127.0.0.1", port=8000)

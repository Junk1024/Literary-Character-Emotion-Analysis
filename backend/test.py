# import pandas as pd
# df = pd.read_csv("video.csv")
# a=df.head(4000)
# a.to_csv('atest.csv',index=False)
# print(df.head(100))
import pandas as pd
import datetime
# 等分csv文件
# path = r'video.csv'
# result_path_dir = r'split/'  #输出文件的路径
# data = pd.read_csv(path)
# # 获取文件总行数
# row_num = len(data)
#
# # 确定每个小文件要包含的数据量
# size = 2000
# j = 1
#
# for start in range(0, row_num, size):
#     stop = start + size
#     filename = "{}\split{}.csv".format(result_path_dir,j)
#     d = data[start: stop]
#     #d['小保单号'] = d['小保单号'].astype(str)
#     print("Saving file : " + filename + ", data size : " + str(len(d)))
#     d.to_csv(filename, index=None)
#     j = j + 1




# 删除换行符
import csv
# path='last.csv'
# with open(path,encoding='utf-8') as fin:
#     with open('video.csv','w',newline='',encoding='utf-8') as fout:
#         r = csv.reader(fin) #读入文件
#         w = csv.writer(fout) #写入文件
#         for row in r:
#             row = [col.replace('\n', '').replace('\r', '') for col in row] #将"\n"替换为无
#             w.writerow(row) #写入新文件
train1=pd.read_csv('split/split1.csv')
train2=pd.read_csv('split/split2.csv')
train3=pd.read_csv('split/split3.csv')
train4=pd.read_csv('split/split4.csv')
train5=pd.read_csv('split/split5.csv')
train6=pd.read_csv('split/split6.csv')
train7=pd.read_csv('split/split7.csv')
train8=pd.read_csv('split/split8.csv')
train11=pd.read_csv('split/split11.csv')
train=pd.concat([train1,train2,train3,train4,train5,train6,train7,train8,train11])
train.to_csv('split/train2.csv',index=False)
# a=pd.read_csv('split/test.csv')
# a.to_csv('split/test1.csv',sep='\t',index=False)
# b=pd.read_csv('split/valid.csv')
# b.to_csv('split/valid1.csv',sep='\t',index=False)

import os
import pandas as pd
import numpy as np

# # 指定文件夹路径
# folder_path = "roledata/"
# # 获取文件夹下的所有文件名
# file_names = os.listdir(folder_path)
# # 打印所有文件名
# for file_name in file_names:
#     print(file_name)
#     #读取文件
#     df1 = pd.read_csv(f'roledata/{file_name}')
#     df2 = pd.read_csv("total.csv")
#     #合并
#     df = pd.concat([df1,df2])
#
#     #保存合并后的文件
#     df.to_csv('total.csv',sep='\t', index=False)
import glob

csv_list=glob.glob('roledata/*.csv')
for i in csv_list:
    fr=open(i,'rb').read()
    with open('last.csv','ab') as f:
        f.write(fr)
    f.close()
print('数据文件合并完成！')

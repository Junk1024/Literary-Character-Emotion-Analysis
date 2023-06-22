# 文学作品人物情感分析系统设计与实现（毕业设计）

## 1、系统目录架构（2023.5.29 已完结）：

![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/content1.png)

## 2、系统功能介绍展示

登录界面用户信息与本地数据库绑定，包括注册登录增删改查。
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/load1.png)
后台首页，可见功能菜单，该系统有两个角色，不同角色功能菜单不同，普通用户无用户管理菜单，该系统没有设置单独的鉴权参数，通过性别来实现简单的不同菜单展示，根据数据库中用户的性别不同返回不同的菜单。
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/index1.png)
数据可视化界面，展示情感分析模型的数据集的信息，还可加载不同用户的用户名
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/data1.png)
用户信息管理界面，对本地数据库的操作，采取了分页处理
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/info1.png)
单文本情感分析界面
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/sentence1.png)
文本级别人物情感分析界面
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/article1.png)
上传 TXT 文档后点击提取人物名单，会将提取结果在前端进行分页展示，可进一步进行文本提取和人物情感分析
![image](https://github.com/Junk1024/Literary-Character-Emotion-Analysis-System/blob/main/img/rolelist1.png)
最终会将人物的所有文本情感分析的分布展示，并基于分布返回人物标签

## 系统启动

前端项目目录下安装依赖，src 目录下使用 node 执行 app.js 启动操作数据库的服务器，后端服务器执行 run.py

答辩结束了，一辩没有过，二辩老师说我做的没有意义，最后还是给我过了。大学四年学到的都用上了，唯一值得庆幸的是毕业设计是自己完成的，以后可能接触不了了，所有代码数据说明书已经开源到我的 GitHub 上，这是我的第一个完整的设计，想必也是最后一个了，各位大佬看看就好。

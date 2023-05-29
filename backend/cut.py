import jieba
text='两个武学名家合力欺侮一个少女，当真好不要脸'
text1='这是治疗蜂毒的蜜浆，拿去给赵志敬罢'
text2='这小子的古怪武功真多'
print(jieba.lcut(text))
print(jieba.lcut(text1))
print(jieba.lcut(text2))


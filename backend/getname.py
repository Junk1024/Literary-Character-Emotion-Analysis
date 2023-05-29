import jieba.posseg as psg
import jieba
def getlist(path):
    with open(path,encoding='utf-8') as f:
        text = f.readlines()
    dict = {}
    jieba.load_userdict('mydict.txt')
    for t in text:
        res = psg.cut(t)
        for item in res:
            if item.flag == 'nr' and item.word in dict:
                dict[item.word] += 1
            elif item.flag == 'nr' and item.word not in dict:
                dict[item.word] = 1
    name_count = sorted(dict.items(), key=lambda x : x[1], reverse=True)
    data=name_count[:100]
    # print(data)
    return data
# getlist('./data/神雕侠侣.txt')
# info=getlist('./data/神雕侠侣.txt')
# print(info)
# path = "./data/神雕侠侣.txt"
# with open(path,encoding='utf-8') as f:
#     text = f.readlines()
# print(text[:10])
# print(len(text))
#
# for t in text:
#     res = psg.cut(t)
#     # print([(item.word, item.flag) for item in res])
# dict = {}
# jieba.load_userdict('mydict.txt')
# for t in text:
#     res = psg.cut(t)
#     for item in res:
#         if item.flag == 'nr' and item.word in dict:
#             dict[item.word] += 1
#         elif item.flag == 'nr' and item.word not in dict:
#             dict[item.word] = 1
# print(dict)
# name_count = sorted(dict.items(), key=lambda x : x[1], reverse=True)
# print(name_count[:30])
# print(str(name_count[:30]))
# role_list=str(name_count[:30])
#
#
# with open("data/roles.txt","w") as f2:
#     for role in name_count[:30]:
#         print(role[0])
#
#         f2.writelines(role[0])
#         f2.writelines('\n')
#
# f2.close()
# f.close()

import os
# line1 = f.readlines()
line1='杨过'
print(line1)
# for l in line1:
#     p = open('./data/1681748147_神雕侠侣1.txt', 'r', encoding='utf-8')
#     line2 = p.readlines()
#     for ll in line2:
#         # print(ll)
#         if l.strip() in ll:
#            # print(ll)
#            # print(l)
#            # print(l.strip())
#            fname=l.strip()
#            q = open(f'./data/extract/{fname}.txt','a+',encoding='utf-8')
#            q.writelines(ll)
def getsentences(name,filepath):
    p = open(filepath, 'r', encoding='utf-8')
    line2 = p.readlines()
    for ll in line2:
        # print(ll)
        if name in ll:
            # print(ll)
            # print(l)
            # print(l.strip())
            fname=name
            q = open(f'./data/extract/{fname}.txt','a+',encoding='utf-8')
            q.writelines(ll)
            p.close()
    str_start = "“"
    str_end   = "”"

    f_orig = open(f'data/extract/{fname}.txt','r', encoding='utf-8') # original file

    f_coord = open(f'data/deepextract/{fname}.txt', 'w')  # target file used to save

    line = f_orig.readline()
    while line:

        # find index according to the key words
        index_start = line.find(str_start)
        index_end = line.find(str_end)
        text = line[index_start : index_end]

        if text != '':
            # If there is more than one [], we can use "Coordinate" and "End" as str_start and str_end
            f_coord.write(str(line[index_start + 1 : index_end]) + '\n')

        line = f_orig.readline()

    f_orig.close()
    f_coord.close()


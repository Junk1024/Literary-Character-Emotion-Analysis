# key words to extract the coordinate
str_start = "“"
str_end   = "”"

f_orig = open('data/extract/洪七公.txt','r', encoding='utf-8') # original file

f_coord = open('data/deepextract/洪七公.txt', 'w')  # target file used to save

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

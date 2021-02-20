#f被称为句柄,负责操纵你打开的这个文件
#       路径
        #绝对路径,相对路径(用的多)
f=open("32_a_txt.txt",mode="r",encoding="utf-8")
print(f.read())
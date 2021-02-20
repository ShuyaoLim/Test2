# lst=["周杰伦","林俊杰","吴克群","潘玮柏"]
# for item in lst:
#     print(item)
    #想看一下索引和元素
# i=0
# while i<len(lst):
#     item=lst[i]
#     print(item) #元素
#     print(i)#索引
#     i+=1
#如何让for循环数数
#range()给for循环搭配使用
# for i in range(10):
#     print(i)
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])
#把列表中找到姓王的,然后把姓王的改成"帅哥"\
lst=["王重阳","谢广坤","刘能","王大能"]
#必须要有索引,还要有元素
for i in range(len(lst)):
    item=lst[i]
    if item.startswith("王"):
        lst[i]="帅哥"
print(lst)


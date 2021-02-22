# lst=[]
#
# for i in range(1,11):
#     lst.append(i)
#
# print(lst)
# #列表推导式的基本语法:[结果 for 循环 if条件]
# lst=[i for i in range(1,11)]
# print(lst)
# #把1-10中的所有奇数添加到列表
# lst=[i for i in range(1,11) if i%2 ==1]
# print(lst)
# #把1-10中的所有奇数的平方添加到列表
# lst=[i **2 for i in range(1,11) if i%2==1 ]
# print(lst)
#
# #python x1 ~python x255
# lst=["python x %s" %i for i in range(1,256)]
# print(lst)

#字典推导式:{key:value for 循环 if}
# lst=["你好","你不好","你很好"]
# d={i:lst[i] for i in range(len(lst))}
# print(d)


#集合推导式 {key for 循环 if}
# lst=["张无忌","张无忌","张三丰"]
# s={item for item in lst}
# print(s)
l=(i +1 for i in range(10))   #python中没有元组推导式 .()生成器表达式
print(l)

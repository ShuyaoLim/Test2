d={"皮长山":"皮校长","王长贵":"谢大脚","谢广坤":"泻立停"}
#1.直接for循环,直接拿到key
# for k in d:
#     print(k)
#     print(d[k])
#2.借助字典keys()
# print(d.keys())
# for k in d.keys():
#     print(k)
#     print(d[k])
#3.拿到所有value
# for v in d.values():
#     print(v)
# #4.通过items()拿到所有的数据
# print(d.items())
for k,v in d.items():
   print(k)
   print(v)
#5.解构
# a=10,20
# print(type(a))
# a,b=(10,20) #解构
# print(a,b)

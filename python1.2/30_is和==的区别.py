a=[10,20,30]
b=[10,20,30]
print(a==b)  #判断两个内容的值是否一致
print(a is b) #判断两个内容的内存地址是否一致

c=None
if c is None:
    print("c是空")
else:
    print("c不是空")
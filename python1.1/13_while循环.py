#模拟无限循环听歌
# while True:
#     print("我们不一样")
#     print("我们都一样")
#     print("我们不一样")
#在没有循环的情况下,如何数数
# print(1)
# print(2)
# print(3)
# i=1
# print(i)
# i=i+1
# print(i)
# i=i+1
# print(i)
# i=1
# while i<=8888:
#     print(i) #8887
#     i=i+1
#从1数到100
# i=1
# while i<=100:
#     print(i)
#     i+=1
#从100数到1
# i=100
# while i>=1:
#     print(i)
#     i-=1
#累加计算
#1+2+3+4.....+100=?
#1.程序得从1数到100
#2.累加计算,每次循环都需要知道上一次循环计算的结果
# i=1
# s=0  #负责保存每次累加的结果
# while i<=100:
#     s=s+i #把i累加
#     i=i+1
# """
# 1           s
# 1           0
# 2           0+1
# 3           0+1+2
# 4           0+1+2+3
# """
# print(s)
flag=True
while flag: #1.while 循环中可以被嵌套   2.结束一个循环的方式,通过改变循环条件
    content=input("请输入你要说的话(Q退出):")
    if content=="Q":
        flag=False
    else:
        print("有人说了:"+content)
# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(3**2)  #次幂计算
# #比较运算
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>=b)
# # print(a<=b)
# a=10
# b=20
# # a=b
# a+=b  #累加计算
# a-=b
# a*=b
# a/=b
# a%=b
# print(a)
# print(b)
# # i=1
# while i<=100:
#     print(i)
#     i+=1

#逻辑运算
#and
#or
#not
# print(True and False)
# print(True or False)
# print(not False)
#() -> not -> and -> or
# print(True or (False and True) or not False and True)
# print(1>2 or 3<4 and 4>6)
# print(1 or 2 and 3)
#当出现数字进行逻辑计算怎么办
#非零当成True
#零当初False
#记住or就可以了,and和or正好相反
#or
# if x==0:
#     结果就是y
# else:
#     结果就是x
#x and y
# #if x==0:
#     结果就是x
#  else:
#     结果就是y
#真实开发中使用and 和or
#登录
# username=input("请输入用户名:")
# password=input("请输入密码:")
# if username =="admin" and password=="123456":
#     print("登录成功")
# else:
#     print("登录失败")
#成员运算
#in not in
#让用户输入评论信息,需要过滤敏感词
#判断敏感词
# content=input("请输入评论:")
# if "苍井空" in content:
#     print("有敏感词")
# else:
#     print("没有敏感词")
#升级需求
#
content=input("请输入评论:")
if "苍井空" in content or "小泽玛利亚"in content:
    print("有敏感词汇")
else:
    print("没有敏感词汇")
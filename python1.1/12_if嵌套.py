#模拟登陆验证
username=input("请输入你的用户名:")
password=input("请输入你的密码:")
if username=='admin':
    pass
    #进一步判断密码是否正确
    if password=="123456":
       print("登录成功")
    else:
        print("对不起,密码错误")
else:
    print("对不起,你输入的用户名不正确")
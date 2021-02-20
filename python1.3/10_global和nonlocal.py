# a=10
# def func():
#     global a #当前func函数内部使用的a都是全局的
#     a=a+1
#     print(a)
# func()
a=10
# def func():
#     global a #把全局内容引入到局部
#     a=20
#     print(a)
# print(a)
# func()
# print(a)
# def func1():
#     a=10
#     def func2():
#         nonlocal a #必须在内部,把外层的xxx变量引入进来
#         a+=1
#         print(a)
#     func2()
# func1()
# print(a)
#只要出现了,在局部改变外层变量,就需要使用global或者nonlocal
flag=False
def login():
    global flag
    username=input(">>>:")
    password=input(">>>:")
    if username=="sylar" and password=='123':
        print("登录成功")
        flag=True
    else:
        print("登录失败")
def add():
    if flag:
        pass
    else:
        print("没登录,请登录...")
def upd():
    pass
def delete():
    pass
def search():
    pass
login()
add()
upd()
search()

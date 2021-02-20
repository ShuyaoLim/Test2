# def func1():
#     print("你好")
#     func2()  #不是函数嵌套,而是函数调用
# def func2():
#     print("你不好")
# func1()
# def func1():
#     print("我是func1")
#     def func2():
#         print("我是func2")
#     print("我是外面")
#     func2() #在func1里面访问func2
# func1()
def func1():
    print("func1_before")
    def func2():
        print("我是func2_before")
        def func3():
            print("我是func3")
            func3()
            print("我是func2_after")
    func2()
    print("func1_after")
func1()
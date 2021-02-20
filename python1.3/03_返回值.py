# def yue():
#     print("约你")
#     print("来吧,特别好玩")
#     return "美女一枚"  #谁调用,返回值就返回给谁
# a=yue()
# print("返回值是:",a)
# def func():
#     print("哈哈")
#     return
#     print("呵呵")
# func()
# def func():
#     print("哈哈哈")
#     print("呵呵呵")
#     return "大姑娘","老娘子","长跪"
# ret=func()
# print("返回值是:",ret)
#1.函数在执行过程中如果遇到return,函数就会理解停止
#2.函数中如果没写return,得到的返回值就是None
#3.函数中写了return,但是没给返回值.此时得到的结果也是None
#4.函数中如果写了return 值.此时有一个返回的结果
#5.函数中如果写了return 值1,值2,值3....此时有多个返回值,外面得到的就是元组.
def func():
    print("去菜市买菜")
    print("买了一条鱼,一棵白菜")
    # return "鱼"
    print("鱼")
    #return和print的区别是什么?????
    #print只是我们目前看到程序运行的一直手段
    #return的结果可以返回给函数外面,函数外面很可能对返回值做进一步的计算
    #

ret=func()
print(ret)
lst=[111,222,333]
ret=lst.pop(0)
print(lst,ret)
# def func(*args): #*表示聚合,把传递过来的位置参数转化成元组
#     print(args)
# lst=["张无忌","张翠山","张三丰"]
#把列表中的每一项当成参数传递给函数func
# func(lst[0],lst[1],lst[2])
#可以借助*来完成打散的操作,可以把可迭代对象转化成位置参数进行传递
# func(*lst)
def func(**kwargs):
    print(kwargs)
dic={"name":"赵敏","age":18}
func(name=dic['name'],age=dic['age'])
func(**dic)
"""
*和**
     在形参:聚合,把位置参数聚合成元组,把关键字参数聚合成字典
     在实参:打散,把可迭代对象转化成位置参数,把字典转化成关键字参数
     
"""
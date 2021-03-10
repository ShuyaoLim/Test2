#先定义类
#类是对象相似数据与功能的集合体
#所以类中最常见的是变量与函数的定义,但是类体其实是可以包含任意其他代码的
#注意:类体代码是在类定义阶段就会执行的,会执行类的名称空间
#再调用类产生对象
class Student:
    #1.变量定义
    stu_school='oldboy'
    def __init__(obj,x,y,z):
        obj.stu_name=x
        obj.stu_age=y
        obj.stu_gender=z
    #2.功能定义
    def tell_stu_info(stu_obj):
        print('学生信息: 名字 :%s 年龄:%s 性别:%s' %(
            stu_obj['stu_name'],
            # stu_obj'stu_age'],
            # stu_obj['stu_gender']
        ))

    def set_info(stu_obj,x,y,z):
        stu_obj['stu_name']=x
        stu_obj['stu_age']=y
        stu_obj['stu_gender']=z

#为对象定制独有的属性
#问题1:代码重复
#问题2: 属性的查找顺序
# stu1_obj=Student()
# stu2_obj=Student()
# stu3_obj=Student()
#
# stu1_obj.stu_name='egon'
# stu1_obj.stu_age=18
# stu1_obj.stu_gender='male'
# print(stu1_obj.__dict__)
#
# stu2_obj.stu_name='lili'
# stu2_obj.stu_age=19
# stu2_obj.stu_gender='female'
# print(stu2_obj.__dict__)
#
# stu3_obj.stu_name='jack'
# stu3_obj.stu_age=20
# stu3_obj.stu_gender='male'
# print(stu3_obj.__dict__)


#解决问题一:
# def init(obj,x,y,z):
#     obj.stu_name=x
#     obj.stu_age=x
#     obj.stu_gender=z
# init(stu1_obj,'egon',18,'male')
# init(stu2_obj,'lili',19,'female')
# init(stu3_obj,'jack',20,'male')
#解决问题二:
#二:再调用类产生对象
#调用类的过程又称之为实例化
#1.先产生一个空对象
#2.python会自动调用类中的__init__方法然后将空对象已经调用类时括号内传入的参数一同传给__init__方法
stu1_obj=Student('egon',18,'male')
stu2_obj=Student('lili',19,'female')
stu3_obj=Student('jack',20,'male')
print(stu1_obj.__dict__)
print(stu2_obj.__dict__)
print(stu3_obj.__dict__)

#总结__init__方法
#1.会再调用类时自动触发执行,用来为对象初始化自己独有数据
#2.__init__内应该存放是为对象初始化属性的功能,但是是可以存放任意其他代码的,想要在
#类调用时就立刻执行的代码都可以放到该方法内
#3.__init__方法必须返回None











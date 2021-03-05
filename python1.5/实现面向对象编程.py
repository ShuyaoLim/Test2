#先定义类
#类是对象相似数据与功能的集合体
#所以类中最常见的是变量与函数的定义,但是类体其实是可以包含任意其他代码的
#注意:类体代码是在类定义阶段就会执行的,会执行类的名称空间
#再调用类产生对象
class Student:
    #1.变量定义
    stu_school='oldboy'
    #2.功能定义
    def tell_stu_info(stu_obj):
        print('学生信息: 名字 :%s 年龄:%s 性别:%s' %(
            stu_obj['stu_name'],
            stu_obj'stu_age'],
            stu_obj['stu_gender']
        ))

    def set_info(stu_obj,x,y,z):
        stu_obj['stu_name']=x
        stu_obj['stu_age']=y
        stu_obj['stu_gender']=z
print(Student.__dict__)
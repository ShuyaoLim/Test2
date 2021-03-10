class Student:
    #1.变量定义
    stu_school='oldboy'
    count=0
    def __init__(self,x,y,z):
        Student.count += 1
        self.stu_name=x
        self.stu_age=y
        self.stu_gender=z
    #2.功能定义
    def tell_stu_info(self):
        print('学生信息: 名字 :%s 年龄:%s 性别:%s' %(
            self['stu_name'],
            # stu_obj'stu_age'],
            # stu_obj['stu_gender']
        ))

    def set_info(self,x,y,z):
        self['stu_name']=x
        self['stu_age']=y
        self['stu_gender']=z
    def choose(self,x):
        print('正在选课')
        self.course=x
stu1_obj=Student('egon',18,'male')
stu2_obj=Student('lili',19,'female')
stu3_obj=Student('jack',20,'male')
print(stu1_obj.count)
print(stu2_obj.count)
print(stu3_obj.count)
#类中存放的是对象共有的数据和功能
#类可以访问
#1.类的数据属性
print(Student.stu_school)
#2.类的函数属性
print(Student.tell_stu_info)
print(Student.set_info)
#二:但其实类中的东西是给对象用的
#1.类的数据属性是共享给所有对象用的,大家访问的地址都一样
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))
Student.stu_school='OLDBOY'
# print(Student.stu_school)
# print(stu1_obj.stu_school)
# print(stu2_obj.stu_school)
# print(stu3_obj.stu_school)

#类的函数属性是绑定给对象用的
# print(Student.tell_stu_info)
# print(Student.set_info)
#绑定方法的特殊之处在于:谁调用绑定方法就会将谁当做第一个参数自动传入
# print(Student.tell_stu_info)
# print(stu1_obj.tell_stu_info)
# print(stu2_obj.tell_stu_info)
# print(stu3_obj.tell_stu_info)
# stu1_obj.tell_stu_info()
# stu2_obj.tell_stu_info()
stu1_obj.choose('python全栈开发')
print(stu1_obj.course)
stu2_obj.choose('linux运维')
print(stu2_obj.course)
stu3_obj.choose('高级架构师')
print(stu3_obj.course)

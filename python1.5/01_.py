def func():
    print()


class Student:
    school='Oldboy'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def choose(self):
        print("%s is choosing a course"%self.name)


stu1=Student('李建刚','男',28)
stu2=Student('王大力','女',18)
print(Student.school)
print(Student.choose)

Student.xxx=1
# print(stu1.xxx)
stu1.xxx=33333333333
# print(stu1.__dict__)

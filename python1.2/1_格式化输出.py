# name=input("请输入名字:")
# age=input("请输入年龄:")
# job=input("请输入工作:")
# hobby=input("请输入爱好:")
#
# # print("-----------info of "+name+"-----------")
# # print("Name :"+name)
# # print("Age :"+age)
# # print("job :"+job)
# # print("hobby :"+hobby)
# # print("----------end------------")
# #字符串格式化
# s="""
# -----------info of %s-----------
# Name :%s
# Age :%s
# job :%s
# hobby :%s
# ----------end------------
# """% (name,name,age,job,hobby)
# print(s)
# #%s表示在字符串中占位,稍后会填充字符串(任何内容)
# #%d 表示在字符串占位整数(dight)
# print("我叫%s,我来自%s，我今年%d" % ("zhoujielun","taiwan",28))
# #%f表示在字符串占位小数(float)
# print("我叫%s,我来自%s,我今年%d,我的收入%.1f" % ("zhoujielun","taiwan",28,22.8))

#新的格式化方案 f-string
name="Shuyao"
addr="a"
hobby="cc"
# print("我叫%s我喜欢在%s做%s"% (name,addr,hobby))
#力推
print(f"我叫{name},我喜欢在{addr}做{hobby}")

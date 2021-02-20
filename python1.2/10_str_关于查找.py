#startwith 判断字符串以xxxxx开头
# name=input("请输入你的名字")
# if name.startswith("张"):
#     print("是的")
# else:
#     print("不是的")
#endwith()判断字符串是否以xxxx结尾
# s="今天天气不错"
# print(s.endswith("天气"))
# print(s.endswith("不错"))
# s="python_java_php_ajax"
# print(s.count("a"))  #计算字符串中出现了几次a
# s="我最喜欢python"
# print(s.find("最"))   #查找字符串找到返回索引,找不到返回-1
# print(s.find("python"))
s="我最喜欢python了"
print(s.index("python"))
print(s.index("#"))   #找不到就报错
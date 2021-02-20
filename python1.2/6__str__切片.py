# s="我最喜欢python"

# print(s[1]+s[2]+s[3])
# print(s[1:4])   #顾头不顾尾  [start:end] end的数据取不到
# print(s[3:]) #:后面啥都不写,表示切到最后、
# print(s[:3]) #:前面啥都不写,表示从头开始切
# print(s[:])  #:前后都不写,从头到尾
# print(s[3:1])  #:默认情况下,切片是从左往右切
#如果需要从右往左切,必须要给出第三个参数
s="abdecfg"
# print(s[5:1:-1])   #fedc
# print(s[1:6:2])
"""
切片的语法:
   s[start: end :step]
   start:起始位置
   end:结束位置(取不到)
   step:步长,每几个出来1个   步长如果是负数,从右向左取,如果是正数,就从左往右取、
   
"""
# s='abcdefghijklmnopqrst'
# print(s[::-2])
# print(s[1:8:3])
# print(s[-1:-7:-2])
# print(s[10:3:-4])
content=input(">>>:")
s=content[::-1] #从右向左切从头切到尾
if s==content:
    print("是回文")
else:
    print("不是回文")
# i=0
# while i<10:
#     print(i)
#     i+=1
# else: #条件不成立,默认执行这里
#     print("ok")
# i=0
# while i<7:
#      if i==7:
#          break
#      print(i)
#      i+=1
# else:
#     print("ok")
#如果执行到break就不执行else
#如果从头到尾都没有执行break,最后一定执行else

#让用户输入一个数字,判断这个数组,是否是质数
n=int(input("请输入一个数字").strip())
#数学:质数是:只能被1和自身整除的数
i=2
while i < n:
    if n %i ==0:
        print("不是质数")
        break
    i+=1
else:
    print("是质数")
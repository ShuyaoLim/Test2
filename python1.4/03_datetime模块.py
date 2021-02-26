from datetime import datetime
from datetime import date
#datetime :年月日,时分秒
#date:年月日
#time 时分秒

# print(datetime.now())
# print(datetime(2018,1,2,12,12,13))

# t1=datetime(2018,1,2,12,30,0)
# t2=datetime(2018,1,4,14,30,0)
# diff=t2-t1
# print(diff.total_seconds())



#格式化一个时间
# t=datetime.now()
#
# print(t.strftime("%Y年%m%d日 %H小时%M分钟%S秒"))  #把时间格式化成一个字符串



#让用户输入两个时间,计算时间差
# s1=input("请输入第一个时间(yyyy-MM-dd HH:MM:SS)")
# s2=input("请输入第二个时间(yyyy-MM-dd HH:MM:SS)")
#
# #把字符串转化成 时间
# t1=datetime.strftime(s1,"%Y-%m%d %H:%M:%S")
# t2=datetime.strftime(s2,"%Y-%m%d %H:%M:%S")
# print(t2-t1)


#date
# print(date.today())
# print(date(1988,12,3))

#必须掌握的内容:
#now()系统时间
#datetime(year,mouth,day,hour,min,second)
#strftime(""%Y-%m%d %H:%M:%S"")  把时间格式化成字符串
#strptime(str,"%Y-%m%d %H:%M:%S")  把字符串转化成时间
#date.today() 今天的日期
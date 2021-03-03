#1.从服务器获取到网页源代码(url.request)
from urllib.request import Request,urlopen
import re
def get_page(url):
    #1.准备请求信息
    r=Request(url,headers={
        #模拟浏览器
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    })
    resp=urlopen(r)
    return resp.read().decode("utf-8")
#2.从网页源代码中提取到你想要的数据(re)
#先准备re
def parse_page(s):
    obj=re.compile(r'<div class="item">.*?<em class="">(?P<rate>.*?)'
                   r'</em>.*?<span class="title"(?P<movie>.*?)</span>.*?<span class="rating_num" property="v:average">'
                   r'(?P<rating_num>.*?)</span>.*?<span>(?P<person_num>.*?)人评价</span>',re.S)   #re.S可以让正则中的.匹配换行符
    res=obj.finditer(s)   #匹配
    for item in res:  #循环结果
        lst=[]
        dic=item.groupdict()  #每次循环都是一个电影的信息
        lst.append(dic)
    return lst
def main():
    f=open("movie.txt",mode="w",encoding="utf-8")
    for i in range(10):
        print()
        s=get_page(f"https://movie.douban.com/top250?start={i*25}&filter=")
        result=parse_page(s)
        for d in result:
            f.write(str(d))
            f.write("\n")
        f.write(str(result))
main()


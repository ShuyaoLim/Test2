# s="中国"
# bs=s.encode("utf-8")
# print(bs)
# bs=b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(type(bs))
# s="中国"
# print(s.encode('gbk'))
#bytes 转化回字符串
bs=b'\xd6\xd0\xb9\xfa'
s=bs.decode("gbk")
print(s.encode("utf-8"))

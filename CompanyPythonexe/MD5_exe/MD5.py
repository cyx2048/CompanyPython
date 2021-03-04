# -*-coding:utf-8-*-
#remark=md5处理

import hashlib

str = input("str=") #需要加密的字符串

def md5Encode(str):
    # 创建md5对象
    m = hashlib.md5()
    m.update(str)  # 传入需要加密的字符串进行MD5加密
    return m.hexdigest()  # 获取到经过MD5加密的字符串并返回

encode_str = md5Encode(str.encode('utf-8')) # 必须先进行转码，否则会报错
print("sign可在output/b.txt文件中查看，"+"sign="+encode_str)

file = open('E:/python_exe/MD5_exe/output/b.txt','w')
file.write("MD5_output"+encode_str)

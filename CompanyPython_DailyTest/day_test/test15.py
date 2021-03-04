"""
编写一个程序，用一个给定的数字作为a的值来计算a+aa+aaa+aaaa的值。
假设向程序提供了以下输入：
9
那么，输出应该是：
11106
"""

i=int(input("i="))
a=i
b=i*10+i
c=i*100+b
d=i*1000+c
y=a+b+c+d
print(y)
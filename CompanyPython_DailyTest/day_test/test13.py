"""
编写一个接受句子并计算字母和数字的程序。
假设向程序提供了以下输入：
hello world! 123
那么，输出应该是：
LETTERS 10
DIGITS 3
"""

s=input("s=")
a=0
b=0
for i in s:
    if i.isdigit():
        a=a+1
    elif i.isalpha():
        b=b+1
    else:
        pass
print("LETTERS:"+str(a))
print("DIGITS:"+str(b))
"""
使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
"""

def outnum(n):
    ls=[]
    i=0
    while i<int(n):
        i=i+1
        if(i%7==0):
            ls.append(i)
        else:
            pass
    print(ls)

n=int(input("n:"))
outnum(n)






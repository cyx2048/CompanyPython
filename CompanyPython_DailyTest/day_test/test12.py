"""
编写一个程序，找出1000到3000之间的所有数字（包括这两个数字），使每个数字都是偶数。
获得的数字应以逗号分隔的顺序打印在一行上。
"""
ls=[]
for i in range(1000,3001):
    if(int(i)%2==0):
        ls.append(i)
print(ls)

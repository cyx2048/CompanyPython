"""
对于给定的整数n，编写一个程序来生成一个字典，其中包含（i，i*i）这样一个介于1和n之间的整数（两者都包括在内）。然后程序应该打印字典。
假设向程序提供了以下输入：8
那么，输出应该是：
{1:1，2:4，3:9，4:16，5:25，6:36，7:49，8:64}
"""

"""第一种方法"""
d={}
i=int(input("input the number:"))
while(i!=0):
    d[i]=i*i
    i=i-1
print(d)

"""第二种方法"""
d={}
i=int(input("input the number:"))
for i in range(1,i+1):
    d[i]=i*i
    i=i-1
print(d)

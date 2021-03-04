"""
编写一个以2位X，Y为输入，生成二维数组的程序。数组的第i行和第j列中的元素值应为i*j。
注：i=0,1…，X-1；j=0,1，…Y-1。

假设程序有以下输入：3,5
那么，程序的输出应该是：
[[0，0，0，0，0]，[0，1，2，3，4]，[0，2，4，6，8]]
"""

str=input("x,y:")
str_list=str.split(",")             #此时已是列表
x=int(str_list[0])
y=int(str_list[1])
# x=int(input("x:"))
# y=int(input("y:"))
i=0
j=0
list=[[0]*y for n in range(x)]        #二维数组的表示法
for i in range(0,x):
    for j in range(0,y):
        list[i][j]=i*j
        j=j+1
    i=i+1
print(list)

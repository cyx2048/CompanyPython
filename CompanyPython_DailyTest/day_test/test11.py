"""
编写一个程序，它接受一系列以逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。可被5整除的数字将按逗号分隔的顺序打印。
例子：
0100,0011,1010,1001,0101
那么输出应该是：
1010
"""
list=[]
x=input("x=")
ls=[x for x in x.split(",")]
#ls=x.split(",")
i=0
for i in ls:
    j=int(i[0])*8+int(i[1])*4+int(i[2])*2+int(i[3])*1
    if(j%5==0):
        list.append(i)
print(",".join(list))



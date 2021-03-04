"""
使用列表理解将列表中的每个奇数平方。列表由一系列逗号分隔的数字输入。

假设向程序提供了以下输入：

1,2,3,4,5,6,7,8,9

那么，输出应该是：

1,3,5,7,9
"""

ls = (input("please input:")).split(',')
ls2 = []
for i in ls:
    if (int(i)%2 != 0):
        ls2.append(int(i)*int(i))
print (ls2)
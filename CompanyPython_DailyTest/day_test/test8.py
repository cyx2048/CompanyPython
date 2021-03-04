"""
编写一个程序，接受以逗号分隔的单词序列作为输入，并在按字母顺序排序后以逗号分隔的序列打印单词。
假设向程序提供了以下输入：without,hello,bag,world
那么，输出应该是：bag,hello,without,world
"""

#方法一直接用内置函数
x=input("input a  string1:")
x_list=[x for x in x.split(",")]  #以逗号隔开，此时已是列表
x_list.sort()
print (','.join(x_list))           #列表中的值以“，”作为连接

#方法二，排序
s=input("input a string2:")
s=s.split(",")
i=0
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        string1=s[i]
        string2=s[i+1]
        if string1[0]>string2[0]:
            b=s[i]
            s[i]=s[i+1]
            s[i+1]=b
        i=i+1
print(",".join(s))




"""
Q= [(2 * C * D)/H]的平方根
C和H的固定值如下：
C是50。H是30。
D是一个变量，其值应以逗号分隔的顺序输入到程序中。
假设程序有以下逗号分隔的输入序列：100,150,180
程序的输出应为：18，22，24
"""
C=50
H=30
ls=[]
"""12 13合成 l=[x for x in input("enter:").split()]"""
x=input("input the list:")
y=x.split(",")                   #split方法,以逗号为分隔符，分割成列表,此时x已是列表
for D in y:
    ls.append(str(int((((2*C*int(D))/H)**(1/2)))))
print (','.join(ls))             #过指定字符(,)连接序列中元素后生成的新字符串。
#print(ls)                       #[18,22]


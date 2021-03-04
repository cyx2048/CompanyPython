"""" 
网站要求用户输入用户名和密码才能注册。编写程序检查用户输入密码的有效性。
以下是检查密码的条件：
1。[a-z]之间至少有一个字母
2。在[0-9]之间至少有一个数字
1。[A-Z]之间至少有一个字母
3。[$#@]中至少有一个字符
4。交易密码最短长度：6
5。交易密码的最大长度：12
您的程序应该接受一系列逗号分隔的密码，并将根据上述标准进行检查。
将打印符合条件的密码，每个密码用逗号分隔。
例子
如果以下密码作为程序的输入：
ABd1234@1,a F1#,2w3E*,2We3345
那么，程序的输出应该是：
ABd1234@1
原文链接：https://blog.csdn.net/weixin_41744624/article/details/103426225
"""

import re
list=[]
x=input("x=").split(",")                   #以逗号隔开，就变成列表
for i in x:
    if(6<len(x) and len(x)<12):
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search('[$#@]',i):
        continue
    elif re.search("\s",i):
        continue
    else:
        pass
    list.append(i)
print(",".join(list))


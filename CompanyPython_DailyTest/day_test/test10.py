"""
编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字顺序排序后打印这些单词。
假设向程序提供了以下输入：
hello world and practice makes perfect and hello world again
那么，输出应该是：
again and hello makes perfect practice world
"""

"""方法1"""
list0=input('please input1').split()
list3=list(set(list0))                       #去重
list3.sort()                                 #排序
print(" ".join(list3))

"""方法2"""
s = input("please input2")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
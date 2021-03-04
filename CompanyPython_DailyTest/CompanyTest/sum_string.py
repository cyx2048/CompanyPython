#coding=UTF-8
#remark=

str='aaabbbbbbcccddddd'
i = 1
curMaxLen = 1
maxLen = 1
l = []
while i <len(str):
    if str[i] == str[i-1]:
        i=i+1
        curMaxLen +=1
    else:
        i += 1
        curMaxLen =1
    if curMaxLen > maxLen:
        maxLen = curMaxLen
        l = str[i - 1]
print(l,maxLen)







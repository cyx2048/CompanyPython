#coding=UTF-8
#remark=


s=input().split(";")
s1=s[1].split(',')
print("The each subject score of  No. %d is %.2f, %.2f, %.2f."%(int(s[0]),float(s1[0]),float(s1[1]),float(s1[2])))
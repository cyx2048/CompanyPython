#coding=UTF-8
#remark=输出第一个只出现一次的字符，如果不存在输出-1

'''
st = input()                          # st = 'abcabceabcf'
dic = {}
l = []

for s in st:                         # dic ={'a':3,'b':3,'c':3,'e':1,'f':1}
    if s not in dic:
        num = st.count(s)
        dic[s]=num

for key in dic.keys():
    if dic[key] == 1:
        l.append(key)                 # l = ['e','f']

if len(l) == 0:
    print(int(-1))
else:
    print(l[0])
'''

'''
st = input()                          # st = 'abcabceabcf'
count = []
for s in st:
    if st.count(s) == 1:
        count.append(s)
if count:
    print(count[0])
else:
    print(-1)
'''



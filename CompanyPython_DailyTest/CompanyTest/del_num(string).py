#coding=UTF-8
#remark=删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

# 统计字母个数  把次数最小的字符挑选出来  再删除

def del_numstring(st):
    # st = 'abcdd'
    new_st=""
    keys = [chr(i+97) for i in range(26)]        # keys=['a','b','c'---'z']
    di = dict.fromkeys(keys,0)                   # di=['a':0,'b':0,'c':0]
    new = []                                     # 字符字数
    keys_s = []                                  # 要删除的字符
    for s in st:
        di[s] = st.count(s)                      # di={'a':1,'b':1,'c':1,'d':2 ,'e':0,'f':0--}
    # print(di)

    for k in di.keys():                          # 将出现次数为0的字符值置为27，以便找到次数最小的值，不然最小的值都是0
        if di[k]==0:
           di[k] = 27                             # di={'a':1,'b':1,'c':1,'d':2，'e':27,'f':27 --}
    for v in di.values():
        new.append(v)                            # new=[1,1,1,2]
    min_num = min(new)                           # 找出次数最小的value值
    for k in di.keys():
        if di[k]==min_num:                       # 找出次数最小的字符列表
            keys_s.append(k)                     # keys_s=['a','b','c']
    for s in st:
        if s not in keys_s:
            new_st=new_st+s
        else:
            pass
    return new_st


while True:
    try:
        st = input()
        if len(st) <= 20:
            print(del_numstring(st))
    except:
        pass

# 找出26个字符出现的次数
# 找出最小的次数字符列表
# 输出字符串
























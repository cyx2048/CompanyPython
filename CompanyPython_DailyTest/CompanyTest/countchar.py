#coding=UTF-8
#remark= 统计字母个数

def countchar(st):
    # st='Abcdefz'
    st.lower()                                # 'abcdefz' s转化为小写
    keys = [chr(i+97) for i in range(26)]    #keys= ['a','b','c'--]
    di = dict.fromkeys(keys,0)               # di={'a':0, 'b':0, 'c':0,--}
    new = []
    for s in st:
        di[s] = st.count(s)

    for v in di.values():
        new.append(v)                      # new=[1,1,1,2]

    return new

if __name__=='__main__':
    st = input()
    str1= ""
    for s in st:
        if s.isalpha() !=0:
            str1 = str1+s          #只有字母才添加到新字符串，标点忽略不计

    print(countchar(st))

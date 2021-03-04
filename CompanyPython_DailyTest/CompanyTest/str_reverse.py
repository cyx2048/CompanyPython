#coding=UTF-8
#remark:字符串反转

# 字符串反转
def string_reverse():
    str = 'abcdef'
    l = list(str)
    l.reverse()
    # 列表转化为字符串
    str1 = ''.join(l)
    print('字符串反转:abcdef>',str1)

# 句子反转  i am boy> boy am i
def sentence_reverse():
    sentence = 'i am boy'
    sentence_list = sentence.split(' ')   # ['1','am','boy']
    sentence_list.reverse()               # ['boy','am','i']
    sentence_str = ' '.join(sentence_list)
    print('句子反转:i am boy>',sentence_str)

# 编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。注意是不同的字符
def statistics_strnum():
    str = 'abcc'
    l = []
    num = 0
    for i in range(len(str)):
        if  str[i] not in l:
            l.append(str[i])
            num = num + 1
    print('计算字符串中含有的不同字符的个数：abcc >',num)

# 输入一个整数，将这个整数以字符串的形式逆序输出  1516000>0006151
def num_reverse():
    num = 1516000
    num_str = str(num)
    num_str_list  = list(num_str)
    num_str_list.reverse()
    result_str = ''.join(num_str_list)
    print('数字颠倒:1516000>',result_str)


#
# if __name__=='__main__':
#     string_reverse()
#     sentence_reverse()
#     statistics_strnum()
#     num_reverse()
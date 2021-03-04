#coding=UTF-8
#remark=

#
# import sys
# d={}
# name=[]
# while True:
#     try:
#         v=raw_input().split(' ')
#         a=v[0].split('\\')[-1]
#         if len(a)>=16:
#             a=a[-16:]
#         else:
#             pass
#         v1=a+' '+str(v[-1])
#         if v1 not in d.keys():
#             name.append(v1)
#             d[v1]=1
#         else:
#             d[v1]+=1
#     except:
#         break
# for item in name[-8:]:
#     sys.stdout.write(item+' '+str(d[item])+'\n')
"""排序"""

"""冒泡排序"""
def function(list):
    count=len(list)
    for i in range(count-1):
        for j in range(i+1,count):
            if list[i]>list[j]:
                a=list[i]
                list[i]=list[j]
                list[j]=a
    return list
s=list(input("list:"))
function(s)
print(s)

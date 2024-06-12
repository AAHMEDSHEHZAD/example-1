def remove_duplication(list1,list2):
    combine=list1,list2
    d=set(combine)
    combine.sort()

    return combine(dict.fromkeys(combine))
list1=[2,3,4,4,5,6,7,8,]
list2=[3,4,8,5,4]
resust=remove_duplication(list1,list2)
print(resust)
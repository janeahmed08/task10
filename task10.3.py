lst=[1,3,4,6,2,3,8,3,3]
count=0
temp=0
index=0
for i in range(0,len(lst)):
    temp=lst.count(lst[i])
    if temp>count:
        count=temp
        index=i
num=lst[index]
print(f"the repeated num is {num}")
print(f"it appeared {count} times")
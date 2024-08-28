lst=[]
n=int(input("enter num of elements"))

for o in range(n):
    elmnts=int(input())
    lst.append(elmnts)

rem_dup=set(lst)
after_rem_dup=list(rem_dup)
after_rem_dup.sort()
if len(after_rem_dup)>1:
    print("the 2nd largest num is ",after_rem_dup[-2])
else:
    print("not found")

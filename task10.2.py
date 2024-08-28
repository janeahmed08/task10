lst=[]
n=int(input("enter num of elements"))
def fmissing(lst,n):
    exp_sum=n*(n+1)/2
    act_sum=sum(lst)
    return exp_sum-act_sum

for i in range(n-1):
    elmnts=int(input())
    lst.append(elmnts)

rem_dup=set(lst)
after_rem_dup=list(rem_dup)
after_rem_dup.sort()
missing_num=fmissing(lst,n)

#for i in range(len(lst)+1) :
 #   if lst[i]<=lst[i+1]==i+1:
  #      continue
   # else:
print("the missing num is ",missing_num)
     #   break
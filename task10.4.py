lst=[5,6,7,8,9,1,2,3,4]
def rotated_c(lst,n):
    min=lst[0]
    min_i=0
    for i in range(0,n):
        if min>lst[i]:
            min=lst[i]
            min_i=i
    return min_i
n=len(lst)
print(rotated_c(lst,n))

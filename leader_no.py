#This program is for the printing leader number in the given array
arr=[16, 17, 4, 31, 5, 21]
nw=[]
l=len(arr)
nw.append(arr[-1])
for i in range(l-2,-1,-1):
    flag=0
    for j in range(i,l):
        if arr[i]<arr[j]:
            flag=1
        else:
            continue   
    if flag!=1:
        nw.append(arr[i])
    else:
        continue    
print(nw)    

     

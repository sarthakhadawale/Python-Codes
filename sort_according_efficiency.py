n=int(input("enter the size of array"))
print("Enter the arry elements")
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)
    else:
        continue
for i in range(0,len(arr2)):
    for j in range(i+1,len(arr2)):
        if arr.count(arr2[i])<arr.count(arr2[j]):
            temp=arr2[i]
            arr2[i]=arr2[j]
            arr2[j]=temp
        elif arr.count(arr2[i])==arr.count(arr2[j]):  
            if arr2[i] > arr2[j]:
                temp=arr2[i]
                arr2[i]=arr2[j]
                arr2[j]=temp
            else:
                continue    
        else:
            continue
print(arr2)
res=[]
for i in arr2:
    l=arr.count(i)
    for j in range(l):  
        res.append(i)     
print(res)  
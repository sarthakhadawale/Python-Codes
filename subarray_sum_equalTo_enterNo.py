n=int(input())
sum=int(input())
arr=[]
for i in range(n):
    in1=int(input())
    arr.append(in1)
count=0    
for i in range(n):
    for j in range(n-1,i-1,-1):
        add=0
        for k in range(j,i-1,-1):
            add=add+arr[k]
            if add==sum:
                count=count+1
            else:
                continue    
print(count)

       





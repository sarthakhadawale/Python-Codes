#this program display that number is prime or not
n=int(input("Enter the number:"))
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag=1
        break
    else:
        continue
if flag!=1:
    print("prime")    
else:
    print("not prime")
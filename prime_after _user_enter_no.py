#this program return the smallest prime number after the user enter number
n=int(input("Enter the number:"))
i=n+1
prime=0
while n<i:
    flag=0  
    for j in range(2,i//2):
        if i%j==0:
            flag=1
            break
        else:
            continue
    if flag!=1:
        prime=i
        print("Smallest prime number after user enter number is:",prime)
        break
    else:
        i=i+1
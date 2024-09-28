#this program display the prime number upto user enter number
rng=int(input("Enter the range :"))
for i in range(2,rng):
    flag=0
    for j in range(2,i//2):
        if i%j==0:
            flag=1
        else:
            continue
    if flag!=1:
        print(i)
    else:
        continue
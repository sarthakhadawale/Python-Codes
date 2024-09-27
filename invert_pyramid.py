n=int(input("Enter"))
c=(n*2)-1
for i in range(n):
    for j in range(c):
        if (j>=i and j<=(c-i-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print(" ") 
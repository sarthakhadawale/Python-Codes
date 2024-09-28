#this program print fibonacci series upto n term
a=0
b=1
n=int(input("Enter the number :"))
print(a)
print(b)
for i in range(n):
    
    c=a+b
    print(c)
    a=b
    b=c




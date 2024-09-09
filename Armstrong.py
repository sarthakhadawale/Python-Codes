l=input("Enter the Number for check armstrong")
list1=list(l)
ln=len(list1)
sum=0
for i in list1:
    k=int(i)
    sum=sum+(k**ln) 
l=int(l) 
if sum==l:
    print("armstrong number")
else:
    print("not armstrong")    
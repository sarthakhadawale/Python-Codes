#print number or string is palindrome
l=input("enter the number to find palindrome or not")
print(l)
list1=list(l)
list2=[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
l1=''.join(list2)
print(l1)
if l==l1:
    print("Palindrome")
else:
    print("Not palindrome")    













   



#Guessing a number in the range 1 to 100 and give response warm,cold and correct on the basis of the correctness of the number.
import random
flag=0
i=0
diff=0
while i<5:
    x=random.randint(1,100)
    choice=int(input("Enter number for gussing"))
    if choice > 100 or choice < 1 :
        print("choice out of bound")
    else:
        diff=abs(x-choice)
        if flag!=1:
            if diff<=10:
                print("warm")
            elif choice==x:    
                print("Gussing is correct")
            else:
                print("cold")   
            flag=1
            diff2=diff
        elif flag==1:
            if diff2>diff:
                print("warmer")
            else:
                print("Colder")  
            diff2=diff     

    i=i+1
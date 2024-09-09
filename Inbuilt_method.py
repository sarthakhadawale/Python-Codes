#It is a module that contain method of factorial,reverse and finding length.

def reverse_print(name):
    """This function is written by sarthak hadawale.
       This function takes input as a string and nuer and gives output in reverse order"""
    l=name
    list1=[]
    for i in range(len(l)-1,-1,-1):
        list1.append(l[i])
    rev="".join(list1)   
    return rev 
def fact(n):
    """This function takes input as number and display the factorial of it"""
    res=1
    for i in range(n,0,-1):
        res=res*i
    return res    

def u_len(l):
    """This Function is written by sarthak hadawale 
       This function take the string as a input and display the length of it"""
    x=str(l)
    ln=0
    for i in x:
        ln=ln+1
    
    return ln        


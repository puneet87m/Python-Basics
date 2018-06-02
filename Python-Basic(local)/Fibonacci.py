"""
Fibonacci series
"""

def fab(num):
    a=1
    b=1
    l=[]
    
    while num:
        l.append(a)
        a,b=b,a+b
        num -= 1
    return(l)    

l2=fab(int(input("enter the number of numbers in the sequence to generate")))
print(l2)


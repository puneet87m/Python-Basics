num=int(input("Enter a number"))
l=[]
i=2
while num > i:
    if num % i == 0:
        l.append(i)
    i = i + 1 
print(l)
 
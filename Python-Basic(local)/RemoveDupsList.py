import random
a=[1,2,3,4,5,1,2,3,4,5,5,5,5]
print(set(a))

y=[]
for i in a:
    if i not in y:
        y.append(i)
         
print(y)    
     
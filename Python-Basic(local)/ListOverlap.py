import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l=[]
for i in a:
    if i in b:
        l.append(i)
print("static list match", l)

x=random.sample(range(10),5)
y=random.sample(range(10),5)
ls=[]
for i in x:
    if i in y:
        ls.append(i)
print("Dynamic list 1",x)
print("Dynamic list 2",y)
print("dynamic list match", ls)


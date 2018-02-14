a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = int(input("Enter a number"))

b = []
for i in a:
    if i < x:
        b.append(i)
print(b)

### One line Solution #####
print([ i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < x])
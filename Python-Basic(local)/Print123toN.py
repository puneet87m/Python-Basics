num = int(input())
n = num -1
summ=0
if len(str(num)) != len(str(n)):
    i=1
else:
    i=0    
while(n > 0):
    i += len(str(n))
    summ += n * 10**i
    n -= 1
print(summ + num)    
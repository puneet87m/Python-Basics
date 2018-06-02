from numpy.lib.function_base import append
# How to find the largest sum of consecutive terms of sequence in a list

arr = [1,2,6,7,8,21,22,23,24,25,7,9,8,1,2,3]
length=len(arr) #7
sum1=0
c=0
final = []
for i in range(length):  #(0,6)
    if i == length-1:
        break
    if arr[i]+1==arr[i+1]:
        if c == 0:
            sum1 = sum1 + arr[i] + arr[i+1]
            c += 1
        else:
            sum1 = sum1 + arr[i+1]    
    else:
        sum1=0
        c=0
    i += 1
    final.append(sum1)       

print(final)     
print(max(final))    
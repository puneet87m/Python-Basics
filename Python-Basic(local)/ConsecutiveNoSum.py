def countConsecutive(N):
     
    # constraint on values of L gives us the 
    # time Complexity as O(N^0.5)
    #
    count = 0
    L = 1
    x = (L * (L + 1)/2)
    print("first x:%f",x )
    while( L * (L + 1) < 2 * N):
        a = (N - (L * (L + 1) ) / 2) / (L + 1)
        print("L:%f",L )
        print("a:%f",a )
        print("integer of a:%f",int(a))
        if (a - int(a) == 0.0):
            count += 1
        L += 1
        x = (L * (L + 1)/2)
        print("next x:%f",x )
        print("===================")
    return count
 
# Driver code
 
N = 15
o=countConsecutive(N)
print(o)
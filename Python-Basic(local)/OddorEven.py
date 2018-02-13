#!/usr/bin/python3
num = int(input("Enter a numbers"))
check = int(input("Enter a numbers(denominator)"))
if num % 4 == 0:
    print("Its an multiple of four")
elif num % 2 == 0: 
    print("Its an even number")
else:
    print("Its an odd number")
            
if num % check == 0:
    print("divides evenly")
else:
    print("Not divides evenly")
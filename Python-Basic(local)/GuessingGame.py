"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user
 to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

Extras:

Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
num=random.randint(1,9)
c = 0
o="Y"

while o.upper() != "E" and o != num:    
    o=input("Whats you guess. To Exit enter E").upper()
    if o.upper() == 'E':
        break
    c = c + 1
    if num < int(o):
        print("Its on lower side. Try again.")
    elif num > int(o):
        print("Its on higher side. Try again.")
    else:
        print("Your guess is right !!!. It took you",c,"tries")
    
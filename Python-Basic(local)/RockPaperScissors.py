"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the 
players want to start a new game)
"""
o="Y"
while o == "Y":    
    Player1 = input("Player1 Enter ROCK/PAPER/SCISSORS").upper()
    Player2 = input("Player2 Enter ROCK/PAPER/SCISSORS").upper()
    if Player1 == 'ROCK' and Player2 == 'SCISSORS' or Player1 == 'SCISSORS' and Player2 == 'PAPER' or Player1 == 'PAPER' and Player2 == 'ROCK': 
        print("Player1 Won !!!")
    elif Player2 == 'ROCK' and Player1 == 'SCISSORS' or Player2 == 'SCISSORS' and Player1 == 'PAPER' or Player2 == 'PAPER' and Player1 == 'ROCK':
        print("Player2 Won !!!")
    elif Player1==Player2:
        print("Its a Tie")
    else:
        print("No one won. Wrong input")    
    o=input("Do u wants to play again Y/N").upper()
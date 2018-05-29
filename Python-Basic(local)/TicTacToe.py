import numpy

game = []


def print_horiz_line():
    print(" ---" * 3)
    
def print_vert_line():
    print("|   " * (3 + 1))
    
#if __name__ == "__main__":


for index in range(3):
    print_horiz_line()
    print_vert_line()
print_horiz_line()


set_r = ()
set_c = ()
def line_match(game):
    for i in range(3):
        set_r = set(game[i])
        if len(set_r) == 1 and game[i][0] != 0:
            return game[i][0]        
    return 0 

def diagonal_match(game):
    if game[1][1] != 0:
        if game[1][1] == game[0][0] == game[2][2]: 
            return game[1][1]
        elif game[1][1] == game[0][2] == game[2][0]:
            return game[1][1]            
    return 0

tarn_game = [[game[j][i] for j in range(len(game))] for i in range(len(game[0]))]

if line_match(game) > 0:
    print(str(line_match(game)) + str(" row wins!"))
#if line_match(numpy.transpose(game)) > 0:
#    print (str(line_match(numpy.transpose(game))) + str(" column wins!"))
if line_match(tarn_game) > 0:
    print (str(line_match(tarn_game)) + str(" column wins!"))
if diagonal_match(game) > 0:
    print (str(diagonal_match(game)) + str(" diagonal wins!"))
    
    
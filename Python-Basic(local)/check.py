def start_game():
    return [[0, 0, 0] for x in range(3)]

def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))
    
def display_game(game):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")

if __name__ == '__main__':
    game = start_game()
    display_game(game)
    player = 1
    winner = 0  # the winner is not yet defined
    
    
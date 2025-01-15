game = [[1, 0, 1],
        [1, 2, 0],
        [1, 2, 1], ]


def win(current_game):
    #     horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"player {row[0]} is the winner horizontaly!!")

    #   digonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player {diags[0]} is the winner diagonaly (/)!!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player {diags[0]} is the winner diagonally (\\)!!")

    #     vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"player {check[0]} is the winner vertically (|)!!")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(
                game_map):  # enumerate helps to itrate through the row along with index,here count is the index.
            print(count, row)  # we can start index by add start keyword along with game,ie game,start=1.

        return game_map
    except IndexError as e:
        print("Error : did you input row/colum as 0 1 or 2 ???", e)
    except Exception as e:
        print("print something went very wrong  !!!! may be because", e)


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = 1
        column_choice = int(input("what column do you want to play (0, 1, 2): "))
        row_choice = int(input("what row do you want to play (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)

# game = game_board(game, just_display=True)
# game = game_board(game_board, player=1, row=3,column=0)

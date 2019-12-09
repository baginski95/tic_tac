# Tic-Tac-Toe

import random
import sys


def print_board(board):
    print(10*'\n') # 10 newlines for nice UI
    print(64*' ' + "    1   2   3")
    print(64*' ' + 3*" " + 11*'-')
    print(64*' ' + 'A', *board[0], sep=" | ", end=" |\n")
    print(64*' ' + "   ---+---+---")
    print(64*' ' + 'B', *board[1], sep=" | ", end=" |\n")
    print(64*' ' + "   ---+---+---")
    print(64*' ' + 'C', *board[2], sep=" | ", end=" |\n")
    print(64*' ' + 3*" " + 11*'-')
    print(64*' ' + 15*'\n')
    return None
def init_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board
def get_move(board, player):
    if player == 1:
        player_name = 'Player_X'
    else:
        player_name = 'Player_O'
    correct = False
    while not correct:
        print_board(board)
        move = input(56 * ' ' + f'{player_name} insert coordinates: ')
        try:
            row = move[0].lower()
            col = move[1]
        except IndexError:
            row = ''
            col = ''
        if move in {'quit', 'q', 'exit', 'wyjście'}:
            quit()
        if row in {'a', 'b', 'c'} and col in {'1', '2', '3'} and len(move) == 2:
            col = int(col) - 1    # It's needed to convert user input
            if row == 'a':        # to numbers of board indexes
                row = 0
            elif row == 'b':
                row = 1
            elif row == 'c':
                row = 2
            if board[row][col] == 'X' or board[row][col] == 'O':
                print('\n' + 63 * ' ' + 'coordinates were used.')
                continue
        else:
            print(58 * ' ' + "You can't use this coordinates.")
            print(48 * ' ' + "Next time try to use: A,B,C for rows and 1,2,3 for columns.")
            continue
        correct = True
        position = (int(row), int(col))
        return position
def mark(board, player, position):
    if player == 1:                 # by getting position from get_move()
        board[position[0]][position[1]] = 'X'
    if player == 2:
        board[position[0]][position[1]] = 'O'
    return board
def has_won(board, player):
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    for row in board:
        if row[0] == mark and row[1] == mark and row[2] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    else:
        return False

def is_full(board):
    empty_fields = 0
    for row in board:
        for field in row:
            if field == ' ':
                empty_fields += 1
    if empty_fields != 0:
        return False
    else:
        return True
def game_pvp():
    board = init_board()
    print_board(board)
    player_X, player_O = 1, 2
    who_won = 0
    end = False
    while not end:
        mark(board, player_X, get_move(board, player_X))
        if has_won(board, player_X):
            who_won = 1
            end = True
            break
        if is_full(board):
            who_won = 3
            end = True
            break
        print_board(board)
        mark(board, player_O, get_move(board, player_O))
        if has_won(board, player_O):
            who_won = 2
            end = True
        if is_full(board):
            who_won = 3
            end = True
        print_board(board)
    print_board(board)
    print_result(who_won)
    if who_won == 1:
        return 1
    if who_won == 2:
        return 2
    if who_won == 3:
        return 3
def print_result(who_won):
    if who_won == 1:
        print(69 * ' ' + 'X won!\n')
    if who_won == 2:
        print(69 * ' ' + 'O won!\n')
    if who_won == 3:
        print(67 * ' ' + "It's a tie!\n")
    return None
def get_random_move_A1(board, moves):
    correct = False
    while not correct:
        if moves == 1 and board[1][1] == ' ':
            row = 1
            col = 1
            moves += 1
            break
        if moves == 2 and (board[0][0] == ' ' or board[0][2] == ' ' or board[2][0] == ' ' or board[2][2] == ' '):
            while True:
                row = random.randrange(0, 3, 2)
                col = random.randrange(0, 3, 2)
                if board[row][col] == 'O' or board[row][col] == 'X':
                    continue
                moves += 1
                break
            break
        if moves == 3 or moves == 4:
            if 'X' in board[1][1] and 'X' in board[0][0] and ' ' in board[2][2]:
                row = 2
                col = 2
                moves += 1
                break
            if 'X' in board[2][2] and 'X' in board[1][1] and ' ' in board[0][0]:
                row = 0
                col = 0
                moves += 1
                break
            if 'X' in board[0][2] and 'X' in board[1][1] and ' ' in board[2][0]:
                row = 2
                col = 0
                moves += 1
                break
            if 'X' in board[1][1] and 'X' in board[2][0] and ' ' in board[0][2]:
                row = 0
                col = 2
                moves += 1
                break
        if moves == 3 or moves == 4:
            for row_index, row_col in enumerate(board, start=0):
                if 'X' in row_col[0] and 'X' in row_col[1] and ' ' in row_col[2]:
                    row = row_index
                    col = 2
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'X' in row_col[0] and 'X' in row_col[2] and ' ' in row_col[1]:
                    row = row_index
                    col = 1
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'X' in row_col[1] and 'X' in row_col[2] and ' ' in row_col[0]:
                    row = row_index
                    col = 0
                    moves +=1
                    position = (int(row), int(col))
                    return position, moves
        if moves == 3 or moves == 4 :
            if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == ' ':
                row = 2
                col = 0
                moves += 1
                break
            if board[0][0] == 'X' and board[2][0] == 'X' and board[1][0] == ' ':
                row = 1
                col = 0
                moves += 1
                break
            if board[1][0] == 'X' and board[2][0] == 'X' and board[0][0] == ' ':
                row = 0
                col = 0
                moves += 1
                break
            if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == ' ':
                row = 2
                col = 1
                moves += 1
                break
            if board[0][1] == 'X' and board[2][1] == 'X' and board[1][1] == ' ':
                row = 1
                col = 1
                moves += 1
                break
            if board[1][1] == 'X' and board[2][1] == 'X' and board[0][1] == ' ':
                row = 0
                col = 1
                moves += 1
                break
            if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == ' ':
                row = 2
                col = 2
                moves += 1
                break
            if board[0][2] == 'X' and board[2][2] == 'X' and board[1][2] == ' ':
                row = 1
                col = 2
                moves += 1
                break
            if board[1][2] == 'X' and board[2][2] == 'X' and board[0][2] == ' ':
                row = 0
                col = 2
                moves += 1
                break
        if moves == 3 or moves == 4:
            for row_index, row_col in enumerate(board, start=0):
                if 'O' in row_col[0] and 'O' in row_col[1] and ' ' in row_col[2]:
                    row = row_index
                    col = 2
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'O' in row_col[0] and 'O' in row_col[2] and ' ' in row_col[1]:
                    row = row_index
                    col = 1
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'O' in row_col[1] and 'O' in row_col[2] and ' ' in row_col[0]:
                    row = row_index
                    col = 0
                    moves +=1
                    position = (int(row), int(col))
                    return position, moves
        if moves == 3 or moves == 4 :
            if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == ' ':
                row = 2
                col = 0
                moves += 1
                break
            if board[0][0] == 'O' and board[2][0] == 'O' and board[1][0] == ' ':
                row = 1
                col = 0
                moves += 1
                break
            if board[1][0] == 'O' and board[2][0] == 'O' and board[0][0] == ' ':
                row = 0
                col = 0
                moves += 1
                break
            if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == ' ':
                row = 2
                col = 1
                moves += 1
                break
            if board[0][1] == 'O' and board[2][1] == 'O' and board[1][1] == ' ':
                row = 1
                col = 1
                moves += 1
                break
            if board[1][1] == 'O' and board[2][1] == 'O' and board[0][1] == ' ':
                row = 0
                col = 1
                moves += 1
                break
            if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == ' ':
                row = 2
                col = 2
                moves += 1
                break
            if board[0][2] == 'O' and board[2][2] == 'O' and board[1][2] == ' ':
                row = 1
                col = 2
                moves += 1
                break
            if board[1][2] == 'O' and board[2][2] == 'O' and board[0][2] == ' ':
                row = 0
                col = 2
                moves += 1
                break
        if moves == 3 or moves == 4:
            for row_index, row_col in enumerate(board, start=0):
                if 'O' in row_col[0] and ' ' in row_col[1] and ' ' in row_col[2]:
                    row = row_index
                    col = 2
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'O' in row_col[1] and ' ' in row_col[0] and ' ' in row_col[2]:
                    row = row_index
                    col = 0
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif 'O' in row_col[2] and ' ' in row_col[1] and ' ' in row_col[0]:
                    row = row_index
                    col = 0
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
        if moves in {1, 2, 3, 4}:
            for row_index, row_col in enumerate(board, start=0):
                if ' ' in row_col[0] and ' ' in row_col[1]:
                    row = row_index
                    col = 0
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif ' ' in row_col[0] and ' ' in row_col[2]:
                    row = row_index
                    col = 2
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
                elif ' ' in row_col[1] and ' ' in row_col[2]:
                    row = row_index
                    col = 2
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
        if moves == 4 and (board[0][0] == ' ' or board[0][2] == ' ' or board[2][0] == ' ' or board[2][2] == ' '):
            row = random.randrange(0, 3, 2)
            col = random.randrange(0, 3, 2)
            moves += 1
        if moves == 4:
            row = random.randrange(0, 3, 2)
            col = random.randrange(0, 3, 2)
            moves += 1
        if moves == 5:
            for row_search, board_row in enumerate(board, start=0):
                for col_search, board_col in enumerate(board_row, start=0):
                    if board[row_search][col_search] == ' ':
                        row = row_search
                        col = col_search
                        moves += 1
                        position = (int(row), int(col))
                        return position, moves
        if board[row][col] == ' ':
            correct = True
    position = (int(row), int(col))
    return position, moves
def game_pve():
    board = init_board()
    print_board(board)
    player_X, player_O = 1, 2
    who_won = 0
    end = False
    moves = 1
    while not end:
        position, moves = get_random_move_A1(board, moves)
        mark(board, player_X, position)
        if has_won(board, player_X):
            who_won = 1
            end = True
            break
        if is_full(board):
            who_won = 3
            end = True
            break
        print_board(board)
        mark(board, player_O, get_move(board, player_O))
        if has_won(board, player_O):
            who_won = 2
            end = True
        if is_full(board):
            who_won = 3
            end = True
        print_board(board)
    print_board(board)
    print_result(who_won)
    if who_won == player_X:
        return 1
    if who_won == player_O:
        return 2
    if who_won == 3:
        return 3
def game():
    again = 'y'
    pX_points_counter = 0
    pO_points_counter = 0
    argument = '--pvp' if len(sys.argv) <= 1 else sys.argv[1]
    while again in {'y', 'yes', 'tak', 'sure', 'YES', 'Yes', 'Y'}:
        if argument in {'--pve', '--single', '--AI', '--computer', 'pve', 'single', '-ai'}:
            give_point_to_winner = game_pve()
        elif argument == '--pvp':
            give_point_to_winner = game_pvp()
        if give_point_to_winner == 1:
            pX_points_counter += 1
        if give_point_to_winner == 2:
            pO_points_counter += 1
        print(50*' ' + f'player_X points: {pX_points_counter}        player_O points: {pO_points_counter}')
        again = input('Would you like to play again? ')
game()

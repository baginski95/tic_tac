# Tic-Tac-Toe

import random
import sys
from math import ceil


def print_board(board):
    INDENTATION = 64
    print(10*'\n')
    print(INDENTATION*' ' + "    1   2   3")
    print(INDENTATION*' ' + 3*" " + 11*'-')
    print(INDENTATION*' ' + 'A', *board[0], sep=" | ", end=" |\n")
    print(INDENTATION*' ' + "   ---+---+---")
    print(INDENTATION*' ' + 'B', *board[1], sep=" | ", end=" |\n")
    print(INDENTATION*' ' + "   ---+---+---")
    print(INDENTATION*' ' + 'C', *board[2], sep=" | ", end=" |\n")
    print(INDENTATION*' ' + 3*" " + 11*'-')
    print(INDENTATION*' ' + 15*'\n')
    return None


def init_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board


def get_move(board, player):  # This function allows check and get coordinates from user input
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
            print(
                48 * ' ' + "Next time try to use: A,B,C for rows and 1,2,3 for columns.")
            continue
        correct = True
        position = (int(row), int(col))
        return position


def mark(board, player, position):  # This function overwrite board
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
        mark_in_row = 0  # If mark_in_row == len(board[0]) in row then player wins
        for field in row:
            if field == mark:
                mark_in_row += 1
        if mark_in_row == len(board):
            return True
    across_mark = 0
    for row in board:
        if row[board.index(row)] == mark:
            across_mark += 1
        if across_mark == len(board):
            return True
    across_mark_reverse = 0
    for row in board:
        if row[len(board) - 1 - board.index(row)] == mark:
            across_mark_reverse += 1
        if across_mark_reverse == len(board):
            return True
    for column_index in range(0, len(board)):
        full_column = 0
        for row_index in range(0, len(board[0])):
            if board[row_index][column_index] == mark:
                full_column += 1
            if full_column == len(board[0]):
                return True


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


def print_result(who_won):
    if who_won == 1:
        print(69 * ' ' + 'X won!\n')  #69 and 67 numbers multiplay indentation 
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
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
        if moves == 3 or moves == 4:
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
                    moves += 1
                    position = (int(row), int(col))
                    return position, moves
        if moves == 3 or moves == 4:
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


def setting_and_checking_move(board, player, position):
    mark(board, player, position)
    if has_won(board, player):
        who_won = player
        end = True
    elif is_full(board):
        who_won = 3
        end = True
    else:
        end = False
        who_won = 0
    print_board(board)
    return end, who_won


def playing_the_game(mode='pvp'):
    board = init_board()
    print_board(board)
    player_X, player_O = 1, 2
    if mode == 'pve':
        moves = 1
    who_won = 0
    end = False
    upper_range = int(ceil(len(board)**2/2))
    for iterate in range(0, upper_range):
        if mode == 'pve':
            position, moves = get_random_move_A1(board, moves)
            end, who_won = setting_and_checking_move(board, player_X, position)
        else:
            end, who_won = setting_and_checking_move(board, player_X, get_move(board, player_X))
        if end:
            break
        end, who_won = setting_and_checking_move(board, player_O, get_move(board, player_O))
        if end:
            break
    print_board(board)
    print_result(who_won)
    if who_won == 1:
        return 1
    if who_won == 2:
        return 2
    if who_won == 3:
        return 3


def game():
    again = 'y'
    pX_points_in_row = 0
    pO_points_in_row = 0
    argument = 'pvp' if len(sys.argv) <= 1 else sys.argv[1]
    while again in {'y', 'yes', 'tak', 'sure', 'YES', 'Yes', 'Y'}:
        if argument in {'--pve', '--single', '--AI', '--computer', 'pve', 'single', '-ai'}:
            give_point_to_winner = playing_the_game(mode='pve')
        elif argument == 'pvp':
            give_point_to_winner = playing_the_game()
            if give_point_to_winner == 1:
                pX_points_in_row += 1
            if give_point_to_winner == 2:
                pO_points_in_row += 1
        print(50*' ' + f'player_X points: {pX_points_in_row}        player_O points: {pO_points_in_row}')
        again = input('Would you like to play again? ')


game()

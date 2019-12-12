#  Tic-Tac-Toe

import sys
import os
from math import ceil
from ai_logic import get_random_move_A1


def get_board_size():
    incorrect_input = True
    terminal_size = os.get_terminal_size()
    terminal_lines = terminal_size.lines
    while incorrect_input:
        try:
            board_size = (input("Insert how many rows and columns should have your board: "))
            board_size = int(board_size)
            if board_size <= 2 or board_size > ((terminal_lines - 4) / 2):  # Terminal size defines max board size
                print(f"You can't create a board with {board_size} size")
                continue
            incorrect_input = False
        except ValueError:
            print(f"Invalid board size: {board_size} ")
            continue
    return board_size


def initial_board(board_size=3):
    board = []
    for board_row in range(board_size):
        board.append([])
        for board_col in range(board_size):
            board[board_row].append(' ')
    return board


def printing_indent(board):
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
    for space in range(int((terminal_width - 4 * len(board))/2)):
        print(' ', sep='', end='')


def print_board(board):
    terminal_size = os.get_terminal_size()
    terminal_lines = terminal_size.lines
    amount_of_new_lines = terminal_lines - 4 - 2 * len(board)
    print('\n' * amount_of_new_lines)
    printing_indent(board)
    print(len(board) * '---+')  # upper frame 
    for row in board:
        printing_indent(board)
        print('|', sep='', end='')
        print(*row, sep=" | ", end=" |\n",)
        printing_indent(board)
        print(len(board) * "---+")


def get_move(board, player):
    if player == 1:
        player_name = 'Player_X'
    else:
        player_name = 'Player_O'
    correct = False
    while not correct:
        print_board(board)
        printing_indent(board)
        move = input(f'{player_name} insert coordinates: ')
        if move in {'quit', 'q', 'exit', 'wyjście'}:
            quit()
        try:
            move = move.split(sep=' ')
            row = int(move[0])
            col = int(move[1])
        except (ValueError, IndexError):
            row = 0
            col = 0
        if 0 < row <= len(board) and 0 < col <= len(board) and len(move) == 2:
            col -= 1  # It's needed to convert user input
            row -= 1  # to numbers of board indexes
            if board[row][col] == 'X' or board[row][col] == 'O':
                printing_indent(board)
                print('coordinates were used.')
                continue
        else:
            printing_indent(board)
            print("You can't use this coordinates.")
            printing_indent(board)
            print(f"Next time try to use numbers from 1 to {len(board)} for rows and columns.")
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
    return end, who_won


def playing_the_game(mode='pvp'):
    if mode == 'pvp':
        board_size = get_board_size()
    if mode == 'pve':
        moves = 1
        board_size = 3  # AI can play just with 3x3 board
    board = initial_board(board_size)
    player_X, player_O = 1, 2
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

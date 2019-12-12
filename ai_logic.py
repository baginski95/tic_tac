# This if logic for AI in Tic_Tac_Toe game
# Only for 3x3 board and AI starts first always

import random


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
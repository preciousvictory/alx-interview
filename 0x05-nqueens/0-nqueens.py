#!/usr/bin/python3
''' N queens puzzle'''
import sys


def del_invalid(board, N, r, c):
    # check forward
    for i in range(c + 1, N):
        board[r][i] = '#'

    # check backward
    for i in range(0, c):
        board[r][i] = '#'

    # check downward
    for x in range(r + 1, N):
        board[x][c] = '#'

    # check upward
    for x in range(0, r):
        board[x][c] = '#'

    # check right up diagonal
    col = c
    for i in range(r - 1, 0, -1):
        col += 1
        if col >= N:
            break
        board[i][col] = '#'

    # check left up diagonal
    col = c
    for i in range(r - 1, 0, -1):
        if col == 0:
            break
        col -= 1
        board[i][col] = '#'
    
    #check right down diagonal
    col = c
    for i in range(r + 1, N):
        col += 1
        if col >= N:
            break
        board[i][col] = '#'

    #check left down diagonal
    col = c
    for i in range(r + 1, N):
        if col == 0:
            break
        col -= 1
        board[i][col] = '#'
    return board


def valid_queen(board, N, start):
    '''valid queens'''
    valid = []

    # start
    board = del_invalid(board, N, 0, start)
    r = 0
    for row in board:
        c = 0
        for col in row:
            if r >= N or c >= N:
                break
            if board[r][c] == 0:
                board = del_invalid(board, N, r, c)
            c += 1
        r += 1

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                valid.append([r, c])
    return valid


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit (1)
        
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit (1)

    if N < 4:
        print('N must be at least 4')
        exit (1)

    for i in range(1, N - 1):
        # initialize board
        board = [[0 for i in range(N)] for j in range(N)]
        valid = valid_queen(board, N, i)
        print(valid)

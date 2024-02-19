board = [' ' for x in range(9)]
def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def empty_squares():
    return ' ' in board
def num_empty_squares():
    return board.count(' ')
def make_move(square, letter):
    board[square]=letter
def undo_move(square):
    board[square]=' '
def winning(board, letter):
    for i in range(0,9,3):
        if board[i]==letter and board[i+1]==letter and board[i+2]==letter:
            return True
    for i in range(3):
        if board[i]==letter and board[i+3]==letter and board[i+6]==letter:
            return True
    if board[0]==letter and board[4]==letter and board[8]==letter:
        return True
    if board[2]==letter and board[4]==letter and board[6]==letter:
        return True
    return False
def minimax(board, depth, alpha, beta, maximizing_player):
    if winning(board, 'O'):
        return {'score': 10}
    elif winning(board, 'X'):
        return {'score': -10}
    elif not empty_squares():
        return {'score': 0}
    if maximizing_player:
        best_move = {'score': -1000}
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                result = minimax(board, depth+1, alpha, beta, False)
                board[i] = ' '
                result['index'] = i
                if result['score'] > best_move['score']:
                    best_move = result
                alpha = max(alpha, best_move['score'])
                if beta<=alpha:
                    break
        return best_move
    else:
        best_move={'score': 1000}
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                result = minimax(board, depth+1, alpha, beta, True)
                board[i]= ' '
                result['index'] = i
                if result['score'] < best_move['score']:
                    best_move = result
                beta = min(beta, best_move['score'])
                if beta <= alpha:
                    break
        return best_move
while empty_squares():
    print_board()
    if num_empty_squares() % 2 == 0:
        move = minimax(board, 0, -1000, 1000, True)['index']
        make_move(move, 'O')
    else:
        move = int(input('Enter your move (0-8): '))
        make_move(move, 'X')
    if winning(board, 'O'):
        print_board()
        print('You Lose!')
        break
    elif winning(board, 'X'):
        print_board()
        print('You Won!')
        break
    elif not empty_squares():
        print_board()
        print('Game Tie.')
        break

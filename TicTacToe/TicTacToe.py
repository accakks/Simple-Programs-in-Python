#Two Player TicTacToe

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWin(board):
    #All Horizontal
    if board['top-L']=='X' and board['top-M']=='X' and board['top-R']=='X':
        winner='X'
    elif board['top-L']=='O' and board['top-M']=='O' and board['top-R']=='O':
        winner='O'
        
    elif board['mid-L']=='X' and board['mid-M']=='X' and board['mid-R']=='X':
        winner='X'
    elif board['mid-L']=='O' and board['mid-M']=='O' and board['mid-R']=='O':
        winner='O'
    elif board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R']=='X':
        winner = 'X'
    elif board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == '0':
        winner = 'O'
    #All vertical
    elif board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L']=='X':
       winner = 'X'
    elif board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O':
       winner = 'O'
    elif board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X':
       winner = 'X'
    elif board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O':
       winner = 'O'
    elif board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R']== 'X':
       winner = 'X'
    elif board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == '0':
       winner = 'O'
    #All Diagonal
    elif board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R']=='X':
       winner = 'X'
    elif board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
       winner = 'O'
    elif board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
       winner = 'X'
    elif board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O':
       winner = 'O'
       
    else:
       winner='none'

    return(winner)
    


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = str(input())
    if (theBoard[move]=='X') or (theBoard[move]=='O'):
        print("\n Invalid move!")
        continue
    else:
       theBoard[move] = turn
       if turn == 'X':
          turn = 'O'
       else:
          turn = 'X'
       wins= checkWin(theBoard)
       if wins!='none':
           break

printBoard(theBoard)
print(wins+" wins!")

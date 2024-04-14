def drawBoard(board): #Board initialization
    row = ''
    print("  a b c d e f g h")
    for i in range(8):
        for j in range(8):
            row += board[i][j] + ' '
        print(i+1, row, i+1)
        row = ''
    print("  a b c d e f g h")

def updateBoard(board): 
    row = ''
    print("  a b c d e f g h")
    for i in range(8):
        for j in range(8):
            row += board[i][j] + ' '
        print(i+1, row, i+1)
        row = ''
    print("  a b c d e f g h")
    updateScore(board, plScore, comScore)

def updateScore(board, plScore, comScore):d
    for i in range(8):
        for j in range(8):
            if (board[i][j] == playerDisk):
                plScore = plScore + 1
            elif (board[i][j] == computerDisk):
                comScore = comScore + 1
    print("Player Score: ", plScore, "Computer Score: ", comScore) 

def settings(playerDisk, computerDisk): #Sets who moves first
    input("Select the maximum depth searched: ")
    first_move = input("Enter 1 to play first, 2 to play second: ")
    if (first_move == "1"):
        print("Player has X, moves first")
        return 'X', 'O'
    else:
        print("Computer has X, moves first")
        return 'O', 'X'

def validMoves(board): #Determines all the possible valid moves
    for i in range(7):
        for j in range(7):
            if (board[i][j] != playerDisk):
                break
            for dirx in range(-1, 1):
                for diry in range(-1, 1):
                    if (dirx == 0 and diry == 0):
                        break
                    if (board[i+dirx][j+diry] == computerDisk):
                        ci = i
                        cj = j
                        while (board[ci+dirx][cj+diry] == computerDisk):
                            ci = ci + dirx
                            cj = cj + dirx
                            if (board[ci+dirx][cj+diry] is "-"):
                                board[ci+dirx][cj+diry] = "V"
                            if ((ci+dirx==0 or ci+dirx==7) and dirx != 0):
                                break
                            if ((cj+diry==0 or cj+diry==7) and diry != 0):
                                break
    return board
               

def isValid(board, posx, posy):
    valBoard = validMoves(board)
    if (valBoard[posx][posy] is "V"):
        return True

def placeDisk(board, posx, posy):
    piecesConverted = 0
    if (isValid):
        if (turn % 2 == 0): 
            for dirx in range(-1, 1):
                for diry in range(-1, 1):
                    i = posx
                    j = posy
                    if (dirx == 0 and diry == 0):
                        break
                    if (board[posx+dirx][posy+diry] == computerDisk):
                        while (board[i+dirx][j+diry] == computerDisk):
                            piecesConverted = piecesConverted + 1
                        if (i+dirx >= 0 and posx+dirx <= 7 and j+diry >= 0 and j+diry <=7):
                            while (i != posx and j != posy):
                                board[i+dirx][j+dirx] = playerDisk
                                i = i - dirx
                                j = j - diry
        else:
            for dirx in range(-1, 1):
                for diry in range(-1, 1):
                    if (dirx == 0 and diry == 0):
                        break
                    if (board[posx+dirx][posy+diry] == playerDisk):
                        while (board[i+dirx][j+diry] == playerDisk):
                            piecesConverted = piecesConverted + 1
    else:
        print("Invalid move.")
    updateBoard(board)

def minimax():
        return 0;

def alpabeta():
    return 0;

turn = 0
plScore, comScore = 0, 0
playerDisk, computerDisk = '', ''
adjacentPositions = [[0,1]]
board = [['-' for i in range(8)] for j in range(8)]
board[3][3], board[3][4], board[4][3], board[4][4] = "O", "X", "X", "O"
drawBoard(board)
playerDisk, computerDisk = settings(playerDisk, computerDisk)
updateScore(board, plScore, comScore)
board = validMoves(board)

while (True):
    if (turn % 2 == 0):
        posx = int(input("Enter row: "))
        posy = int(input("Enter column: "))
        if (posx >= 0 and posx < 8):
            if (posy >= 0 and posy < 8):
                placeDisk(board, posx, posy)
                updateBoard(board)
        else:
            print("Invalid move")
    else:
        minimax()
    turn = turn + 1

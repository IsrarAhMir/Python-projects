import random 

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentPlayer = 'X'
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " +  board[2])
    print("___________")
    print(board[3] + " | " + board[4] + " | " +  board[5])
    print("___________")
    print(board[6] + " | " + board[7] + " | " +  board[8])

def playerInput(board):
    inp = int(input(f"Player {currentPlayer}, enter your move (1-9): "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Oops! That spot is already taken.")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    return False

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkDraw(board):
    global gameRunning
    if "_" not in board:
        print("It's a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        print(f"The winner is {winner}!")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            break

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkDraw(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkDraw(board)
    switchPlayer()

# python tic tac toe AI
import random
currentPlayer = "X"
gameRunning = True
winner = None
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def printBoard(board):
    print(board[0] + "  " + board[1] + "  " + board[2])
    print(board[3] + "  " + board[4] + "  " + board[5])
    print(board[6] + "  " + board[7] + "  " + board[8])


# print board

# player input

# check if win / tie

# switch player

# check if win

def playerInput(board):
    inp = int(input("Select a spot (1-9): "))
    if inp < 1 or inp > 9 or not isinstance(inp, int):
        print("Invalid input")
    if board[inp - 1] != "O":
        board[inp - 1] = currentPlayer
    else:
        print("Player already at that spot!")

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-" and board[1] != "-" and board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" and board[4] != "-" and board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-" and board[7] != "-" and board[8] != "-":
        winner = board[6]
        return True
    else:
        return False


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-" and board[3] != "-" and board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-" and board[1] != "-" and board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-" and board[5] != "-" and board[8] != "-":
        winner = board[2]
        return True
    else:
        return False


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-" and board[4] != "-" and board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-" and board[4] != "-" and board[6] != "-":
        winner = board[2]
        return True
    else:
        return False



def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False
    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False
    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

# if player selects easy mode
def switchPlayerEasy():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    while currentPlayer == "O":
        cpuPos = random.randint(0,8)
        if board[cpuPos] != "X":
            board[cpuPos] = "O"
            currentPlayer = "X"


def blockRow(board):
    if board[0] == board[1] == "X":
        board[2] = currentPlayer
        return True
    elif board[2] == board[1] == "X":
        board[0] = currentPlayer
        return True
    elif board[3] == board[4] == "X":
        board[5] = currentPlayer
        return True
    elif board[5] == board[4] == "X":
        board[3] = currentPlayer
        return True
    elif board[6] == board[7] == "X":
        board[8] = currentPlayer
        return True
    elif board[8] == board[7] == "X":
        board[6] = currentPlayer
        return True

def blockCol(board):
    if board[0] == board[3] == "X":
        board[6] = currentPlayer
        return True
    elif board[6] == board[3] == "X":
        board[0] = currentPlayer
        return True
    elif board[1] == board[4] == "X":
        board[7] = currentPlayer
        return True
    elif board[7] == board[4] == "X":
        board[1] = currentPlayer
        return True
    elif board[2] == board[5] == "X":
        board[8] = currentPlayer
        return True
    elif board[8] == board[5] == "X":
        board[2] = currentPlayer
        return True


def blockDiag(board):
    if board[0] == board[4] == "X":
        board[8] = currentPlayer
        return True
    elif board[2] == board[4] == "X":
        board[6] = currentPlayer
        return True
    else:
        if board[4] == "-":
            board[4] = currentPlayer


def switchPlayerHard(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    while currentPlayer == "O":
        blockRow(board)
        blockCol(board)
        blockDiag(board)


print("1: Easy\n2: Hard")
mode = input("Select your mode: ")
while gameRunning:
    printBoard(board)
    playerInput(board)
    if mode == "1":
        switchPlayerEasy()
    else:
        switchPlayerHard(board)
    checkIfWin(board)
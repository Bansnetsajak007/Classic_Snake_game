# classic snake game written in python (terminal based)

#work in progress

#Iam assuming here i will be wasting 6-7 hours of my life
import random

def displayScore():
    score = 100
    print(f"\nscore:{score}")
    print()

def displayBoard(board):
    for row in board:
        print(' '.join(row))


def gameBoard(size = 30):
    #formatted method more python type
    board = [[' ' for _ in range(size)] for _ in range(size)]

    for i in range(size):
        board[i][0] = 'H'
        board[i][size -1 ] = 'H'
        board[0][i] = 'H'
        board[size - 1][i] = 'H'

    return board


def generateFood(board):
    totalSize = len(board)

    #Generating food randomly using coordinates
    while True:
        row = random.randint(1, totalSize - 2)
        column = random.randint(1, totalSize - 2)

        if(board[row][column] == ' '):
            board[row][column] = 'F' #displaying food as F
            break

if __name__ == "__main__":

    displayScore()
    board = gameBoard()
    generateFood(board)
    displayBoard(board)
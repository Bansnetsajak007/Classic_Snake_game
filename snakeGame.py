# classic snake game written in python (terminal based)

#work in progress

#Iam assuming here i will be wasting 6-7 hours of my life

def gameBoard():
    size = 10
    for i in range(0,size):
        for j in range(0,size):
            if(i == 0 or i == size - 1 or j == 0 or j == size - 1):
                print("0  ",end="")
            else:
                print("   ",end="")
                
        print("\n")


def displayScore():
    score = 100
    print(f"\nscore:{score}")
    print()


if __name__ == "__main__":

    displayScore()
    gameBoard()
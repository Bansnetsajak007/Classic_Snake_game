# classic snake game written in python (terminal based)

#work in progres
#Iam assuming here i will be wasting 6-7 hours of my life

import random
import os
import msvcrt
import time

# Initialize variables
height = 20
width = 20
game_over = False
score = 0
x, y = height // 2, width // 2
fruit_x, fruit_y = 0, 0
flag = 0

# Function to generate the fruit within the boundary
def setup():
    global x, y, fruit_x, fruit_y, score, game_over
    game_over = False
    x = height // 2
    y = width // 2

    # Generate random fruit coordinates
    fruit_x = random.randint(1, height - 2)
    fruit_y = random.randint(1, width - 2)
    score = 0

# Function to draw the boundaries
def draw():
    os.system('cls')
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("#", end="")
            else:
                if i == x and j == y:
                    print("0", end="")
                elif i == fruit_x and j == fruit_y:
                    print("F", end="")
                else:
                    print(" ", end="")
        print()
    print("Score =", score)
    print("Press X to quit the game")

# Function to take input
def input_key():
    global flag, game_over
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == 'a':
            flag = 1
        elif key == 's':
            flag = 2
        elif key == 'd':
            flag = 3
        elif key == 'w':
            flag = 4
        elif key == 'x':
            game_over = True

# Function for the logic behind each movement
def logic():
    global x, y, flag, score, game_over, fruit_x, fruit_y
    time.sleep(0.01)
    if flag == 1:
        y -= 1
    elif flag == 2:
        x += 1
    elif flag == 3:
        y += 1
    elif flag == 4:
        x -= 1

    # Check if the game is over
    if x < 0 or x >= height or y < 0 or y >= width:
        game_over = True

    # If snake reaches the fruit
    if x == fruit_x and y == fruit_y:
        # Generate a new fruit
        fruit_x = random.randint(1, height - 2)
        fruit_y = random.randint(1, width - 2)
        score += 10

# Driver code
def main():
    setup()
    while not game_over:
        draw()
        input_key()
        logic()

if __name__ == "__main__":
    main()

import os
os.system("cls")

game = [[' ' for x in range(3)] for y in range(3)]
pturn = 1
tilex = 0
tiley = 0
winner = 0

def clamp(n, mi, ma): return max(mi, min(ma, n))

class style():
    HOVER = '\033[44m\033[01m'
    RESET = '\033[0m'

def draw():
    global tilex, tiley
    os.system("cls")
    print("")
    
    for y in range(3):
        for x in range(3):
            if x == 1 or x == 2: print(style.RESET, "|", end='', sep='')
            if x == tilex and y == tiley:
                print(style.HOVER, " " + str(game[x][y]) + " ", end='', sep='')
            else:
                print(style.RESET, " " + str(game[x][y]) + " ", end='', sep='')

        print("", sep='')
        if y == 0 or y == 1: print(style.RESET, "---|---|---", sep='')

    print(style.RESET, "\nPlayer " + str(pturn) + "'s turn!")

def uinput():
    global tilex, tiley
    i = input("").lower()
    if i == 'w': tiley -= 1
    if i == 'a': tilex -= 1
    if i == 's': tiley += 1
    if i == 'd': tilex += 1
    if i == 'p': place(tilex, tiley)
    if i == 'quit': quit()
    
    tilex = clamp(tilex, 0, 2)
    tiley = clamp(tiley, 0, 2)

    return i

def place(x, y):
    global pturn
    if pturn == 1:
        game[x][y] = 'X'
        pturn = 2
    elif pturn == 2:
        game[x][y] = 'O'
        pturn = 1

x = [ 0, 0, 0, 0 ]
o = [ 0, 0, 0, 0 ]

def check():
    global winner
    for n in range(3):
        for h in range(3): # Horizontal
            if x[0] == h:
                if game[h][n] == 'X': x[0] += 1
            if o[0] == h:
                if game[h][n] == 'O': o[0] += 1

        for v in range(3): # Vertical
            if x[1] == v:
                if game[n][v] == 'X': x[1] += 1
            if o[1] == h:
                if game[n][v] == 'O': o[1] += 1

        if x[2] == n: # Left to right diagonal
            if game[n][n] == 'X': x[2] += 1
        if o[2] == n:
            if game[n][n] == 'O': o[2] += 1

        if x[3] == n: # Right to left diagonal
            if game[2-n][n] == 'X': x[3] += 1
        if o[3] == n:
            if game[2-n][n] == 'O': o[3] += 1

    for i in range(4):
        if x[i] == 3: winner = 1
        if o[i] == 3: winner = 2

while True:
    os.system("cls")
    draw()

    if winner != 0:
        print("\nPlayer {0} wins!".format(winner))
        input("")
        quit()
        
    uinput()
    check()
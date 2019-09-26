#tictactoe

def userinput(x,y,z):
    x = input('\nWhat ' + z + """ would you like to play on?(1-3)
>""")

    try:
        x = int(x)
    except ValueError:
        print('\nNon-integer input')
        y = y - 1
        return 3,y
    else:
        return (x-1),y
def playerTurn(x,y,z,a):
    if x == 3 or y == 3:
        print('\nTry Again!')
    elif z[x][y] != 0:
        print('\nPlace has already been used')
        a = a - 1
    else:
        if (int(a) % 2) == 0:
            z[x][y] = 'x'
        else:
            z[x][y] = 'o'
    for i in range(3):
        print(z[i])
    return a

def check(x,y):
    if x == y - 2:
        x = x + 1
        return x
    else:
        return x

def winCheck(x,z):
    if z == 'x':
        y = 1
    elif z == 'o':
        y = 2
    for i in range(3):
        if x[i].count(z) == 3:
            return 1,y
        elif x[0][i] == z and x[1][i] == z and x[2][i] == z:
            return 1,y
    if (x[0][0] == z and x[1][1] == z and x[2][2] == z) or (x[0][2] == z and x[1][1] == z and x[2][0] == z):
        return 1,y
    else:
        return 0,0


board = [[0,0,0],
         [0,0,0],
         [0,0,0]] #z

player1 = 'x'
player2 = 'o'
turn = 0 #a
game = 0
row = 0#x
place = 0#y
rowStr = 'row'
placeStr = 'place'
count = 0
winner = 0
while game != 1:
    count = turn
    row,turn = userinput(row,turn,rowStr)
    place,turn = userinput(place,turn,placeStr)
    turn = check(turn,count)
    turn = playerTurn(row,place,board,turn)
    turn = check(turn,count)
    turn = turn + 1
    game,winner = winCheck(board,player1)
    if game == 1:
        break
    game,winner = winCheck(board,player2)
print('\nThe winner is Player' + str(winner))

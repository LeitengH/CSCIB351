HEIGHT = 15
WIDTH = 15
board = [[[] for y in range(HEIGHT)] for x in range(WIDTH)]
for i in range (0, HEIGHT):
    for j in range (0, WIDTH):
        board[i][j] = 0  # fill 0 in it
        
def printBoard(WIDTH,HEIGHT):
    print("")
    print("+" + "---+" * WIDTH)
    for rowNum in range(HEIGHT - 1, -1, -1):
        row = "|"
        for colNum in range(WIDTH):
            if len(board[colNum]) > rowNum:
                row += " " + ('X' if board[colNum][rowNum] else 'O') + " |"
            else:
                row += "   |"
        print(row)
        print("+" + "---+" * WIDTH)

print(printBoard(15, 15))

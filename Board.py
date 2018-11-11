#Group number 7
#Leiteng Huang, Chang Liu, Jie Tang
#Final Project
#Last edit on: 11/11/2018

##################################   Board Class   ##################################
# The Board class is the data structure that holds the Gomoku and the game operations

# The Gomoku board is 15 * 15 cells tall and wide

# The underlying data structure is a 2-d list
# The first dimension is the row; the second dimension is the column;
# Note: We init all cells to 0 at the beginning, and update after every step.

# Every cell in the above list contains either a 1 or 2 is represented by 1 tiles, and Player
# 2 is represented by 2 titles.
#####################################################################################
import copy #use copy to copy 2d array

class Board(object):

    HEIGHT = 15 # our board is a 15 * 15 cells baord
    WIDTH = 15

    ########################   Constructor   ###############################
    #
    #
    #  No arguments --> Creates a brand new empty board
    #
    #  orig         --> If you pass an existing board as the orig argument,
    #                   this will create a copy of that board
    #
    ########################################################################
    def __init__(self, orig = None):

        # copy
        if(orig):
            self.board = orig.board.copy()
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return



        # create new board
        else:
            self.board = [[[] for y in range(self.HEIGHT)] for x in range(self.WIDTH)]
            for i in range (0, HEIGHT):
                for j in range (0, WIDTH):
                    self.board[i][j] = 0  # fill 0 in it
            self.numMoves = 0
            self.lastMove = None
            return

    ########################################################################
    #                           Mutations
    ########################################################################

    # Puts a pirce in the appropriate column and checks to see if it was a winning move
    # Pieces are either 1 or 0; automatically decided
    # NOTE: does NOT check if the move is valid
    def makeMove(self, row, column):
        #update board data
        piece = self.numMoves % 2
        self.lastMove = [piece, row, column]
        self.numMoves += 1
        self.board[row][column] = piece


    ########################################################################
    #                           Observations
    ########################################################################

    # Returns:
    #  -1 if game is not over
    #   0 if the game is a draw
    #   1 if player 1 wins
    #   2 if player 2 wins
    def isTerminal(self):
        pass



    ########################################################################
    #                           Utilities
    ########################################################################

    # Return true iff the game is full
    def isFull(self):
        return self.numMoves == 225

    # Prints out a visual representation of the board
    # X's are 1's and 0's are 0s
    def printBoard(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)




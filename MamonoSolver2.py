from MamonoSweeperGame import MamonoSweeper
import random

class MamonoSolver2:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.solve()

    def solve(self):
        # Generating random
        row = random.randint(0, self.mamonoGame.row_size-1)
        col = random.randint(0, self.mamonoGame.col_size-1)

        self.mamonoGame.input(str(row) + " " + str(col))

        #while self.mamonoGame.is_playing == True:

    def printBoards(self):
        #  print solver board
        print("\n===========================================================================")
        print("================================ GameBoard ================================")
        print("===========================================================================")

        self.mamonoGame.print_board()
        
        print("\n===========================================================================")
        print("============================== SolutionBoard ==============================")
        print("===========================================================================")

        self.mamonoGame.print_solution()
        
from MamonoSweeperGame import MamonoSweeper
import random

class MamonoSolverRand:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.solve()

    def solve(self):
        while self.mamonoGame.is_playing == True:
            self.clickRandom()
        if self.mamonoGame.player_won:
            # print("You Win!")
            pass
        else:
            # print("You Died!")
            pass

    def checkWin(self):
        return self.mamonoGame.player_won

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

    def clickRandom(self):
        # Generating random
        row = random.randint(0, self.mamonoGame.row_size-1)
        col = random.randint(0, self.mamonoGame.col_size-1)

        # First move
        self.mamonoGame.input(str(row) + " " + str(col))
        
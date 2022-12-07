from MamonoSweeperGame import MamonoSweeper
import random

class MamonoSolver2:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.solve()

    def solve(self):
        # Generating random
        row = random.randint(0, self.row_size-1)
        col = random.randint(0, self.col_size-1)

        self.mamonoGame.input(str(row) + " " + str(col))

        #while self.mamonoGame.is_playing == True:

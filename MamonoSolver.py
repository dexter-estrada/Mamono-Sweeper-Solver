from MamonoSweeperGame import MamonoSweeper

class MamonoSolver:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.mamonoSolverBoard = MamonoSweeper()
        self.solve()

    def solve(self):
        loop = True

        if all(i == ' ' for i in self.mamonoSolverBoard.mine_values):  # if board is empty
            # start in top left corner [0,0]
            self.mamonoGame.input("0 0")
            self.mamonoSolverBoard.input("0 0")

        while(loop):
            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    if self.mamonoGame.level == self.mamonoGame.mine_values[r][c] and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are equal to level
                        for n in mamonoGame.neighbors(r, c):
                            self.mamonoGame.input(str(n[0]) + " " + str(n[1]))
                            self.mamonoSolverBoard.input(str(n[0]) + " " + str(n[1]))
                        break

                    if self.mamonoSolverBoard[r][c] < 0:  # if solver board has negative values, change them
                        pass

    def isNeighborsCleared(self, r, c):
        cleared = True

        for n in mamonoSolverBoard.neighbors(r, c):
            if mamonoSolverBoard.mine_values[n[0]][n[1]] == " ":
                return False

        return cleared



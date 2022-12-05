from MamonoSweeperGame import MamonoSweeper
import copy

class MamonoSolver:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.mamonoSolverBoard = copy.deepcopy(mamonoGame)
        self.solve()

    def solve(self):
        loop = True

        if all(i == [' '] * self.mamonoSolverBoard.row_size for i in self.mamonoSolverBoard.monster_val):  # if board is empty
            # start in top left corner [0,0]
            self.mamonoGame.input("0 0")
            self.mamonoSolverBoard.input("0 0")

        counter = 0
        while loop:
            counter += 1
            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    if self.mamonoGame.monster_val[r][c] == ' ':
                        continue
                    elif self.mamonoGame.lvl == int(self.mamonoSolverBoard.monster_val[r][c]) and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are equal to level
                        for n in self.mamonoGame.neighbors(r, c):
                            self.mamonoGame.input(str(n[0]) + " " + str(n[1]))
                            self.mamonoSolverBoard.input(str(n[0]) + " " + str(n[1]))
                        break
                    elif int(self.mamonoSolverBoard.monster_val[r][c]) < 0:  # if solver board has negative values, update solver neighbors
                        self.mamonoSolverBoard.monster_val[r][c] = 0

                        for n in self.mamonoGame.neighbors(r, c):
                            if self.mamonoSolverBoard.monster_val[n[0]][n[1]] != ' ' and self.mamonoSolverBoard.monster_val[n[0]][n[1]]-1 > 0:
                                self.mamonoSolverBoard.monster_val[n[0]][n[1]] -= 1


            if counter == 30:  # temporarily run loop 30 times
                loop = False

        print("counter: " + str(counter))

    def printBoards(self):
        #  print solver board
        print("\n===========================================================================")
        print("================================ GameBoard ================================")
        print("===========================================================================")

        self.mamonoGame.print_board()

        print("\n===========================================================================")
        print("=============================== SolverBoard ===============================")
        print("===========================================================================")

        self.mamonoSolverBoard.print_board()
    """
        print("\n===========================================================================")
        print("============================== SolutionBoard ==============================")
        print("===========================================================================")

        self.mamonoGame.print_solution()
    """
    def isNeighborsCleared(self, r, c):
        for n in self.mamonoGame.neighbors(r, c):
            if self.mamonoGame.monster_val[n[0]][n[1]] == ' ':
                return False

        return True

    def clearNeighbors(self, r, c):
        for n in self.mamonoGame.neighbors(r, c):
            if self.mamonoGame.monster_val[n[0]][n[1]] == ' ':
                self.mamonoGame.input(str(n[0]) + " " + str(n[1]))
                self.mamonoSolverBoard.input(str(n[0]) + " " + str(n[1]))


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
                    game_value = self.mamonoGame.monster_val[r][c]
                    solver_value = self.mamonoSolverBoard.monster_val[r][c]

                    if not self.isNum(game_value) or not self.isNum(solver_value):
                        continue
                    elif self.mamonoSolverBoard.lvl >= int(solver_value) > 0 and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are greater to level
                        for n in self.mamonoGame.neighbors(r, c):
                            self.solverInput(n[0], n[1])
                        break
                    elif solver_value < 0:  # if solver board has negative values, update solver neighbors
                        self.mamonoSolverBoard.input(str(r) + " " + str(c) + " " + str(-solver_value))  # flag it
                        for n in self.mamonoSolverBoard.neighbors(r, c):  # make neighbors subtract by solver value
                            neighbor = self.mamonoSolverBoard.monster_val[n[0]][n[1]]
                            if self.isNum(neighbor) and ((int(neighbor) + int(solver_value)) > 0):
                                # print(self.mamonoSolverBoard.monster_val[n[0]][n[1]])
                                self.mamonoSolverBoard.monster_val[n[0]][n[1]] += solver_value

            if counter == 30:  # temporarily run loop 30 times
                loop = False

        print("counter: " + str(counter))

    # checks if given value is a number (includes negatives), only checks ' ' and 'f'
    def isNum(self, num):
        if str(num) == ' ':
            return False
        elif "F" in str(num):
            return False

        return True

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
        for n in self.mamonoSolverBoard.neighbors(r, c):
            if self.mamonoSolverBoard.monster_val[n[0]][n[1]] == ' ':
                self.mamonoGame.input(str(n[0]) + " " + str(n[1]))
                self.mamonoSolverBoard.input(str(n[0]) + " " + str(n[1]))

    def solverInput(self, r, c, f=-1):  # calls input from game on solver and regular board, checks for flagged monsters
        input_string = str(r) + " " + str(c)
        solver_value = self.mamonoSolverBoard.monster_val[r][c]
        if f > 0:
            input_string += " " + str(f)

        self.mamonoGame.input(input_string)
        self.mamonoSolverBoard.input(input_string)

        if f < 0:  # if no flag is inputted, check neighbors for flags
            for n in self.mamonoSolverBoard.neighbors(r, c):
                if self.isNum(solver_value) and tuple(n) in self.mamonoSolverBoard.flags.keys():
                    # print("flag " + self.mamonoSolverBoard.monster_val[n[0]][n[1]][1]
                    print(self.mamonoSolverBoard.monster_val[n[0]][n[1]][1])
                    solver_value -= int(self.mamonoSolverBoard.monster_val[n[0]][n[1]][1])







from MamonoSweeperGame import MamonoSweeper
import copy


class MamonoSolver:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.mamonoSolverBoard = [[' ' for y in range(self.mamonoGame.board_size)] for x in range(self.mamonoGame.board_size)]
        self.subtractedMonsters = dict()  # Key = (row, col): value = monster level (negative)
        self.solve()

    def solve(self):
        loop = True

        if all(i == [' '] * self.mamonoGame.row_size for i in self.mamonoSolverBoard):  # if board is empty
            # start in top left corner [0,0]
            self.mamonoGame.input("0 0")
            self.mamonoSolverBoard[0][0] = self.mamonoGame.monster_val[0][0]

        counter = 0
        while loop:
            counter += 1
            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    game_value = self.mamonoGame.monster_val[r][c]
                    solver_value = self.mamonoSolverBoard[r][c]

                    if not self.isNum(game_value) or not self.isNum(solver_value):
                        continue
                    elif solver_value == 0:
                        self.clearNeighbors(r, c)

                    elif self.mamonoGame.lvl >= int(solver_value) > 0 and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are greater to level
                        for n in self.mamonoGame.neighbors(r, c):
                            self.solverInput(n[0], n[1])
                        break
                    elif solver_value < 0:  # if solver board has negative values, update solver neighbors
                        self.subtractedMonsters[(r, c)] = solver_value
                        for n in self.mamonoGame.neighbors(r, c):  # make neighbors subtract by solver value
                            neighbor = self.mamonoSolverBoard[n[0]][n[1]]
                            if self.isNum(neighbor):
                                # print(self.mamonoSolverBoard.monster_val[n[0]][n[1]])
                                self.mamonoSolverBoard[n[0]][n[1]] += solver_value

            if counter == 30:  # temporarily run loop 30 times
                print(self.subtractedMonsters)
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

        for row in self.mamonoSolverBoard:
            print(row)

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
            if self.mamonoSolverBoard[n[0]][n[1]] == ' ':
                self.solverInput(n[0], n[1])

    def solverInput(self, r, c, f=-1):  # calls input from game on solver and regular board, checks for flagged monsters
        input_string = str(r) + " " + str(c)
        if f > 0:
            input_string += " " + str(f)

        self.mamonoGame.input(input_string)
        self.mamonoSolverBoard[r][c] = self.mamonoGame.monster_val[r][c]
        print(self.mamonoGame.monster_val[r][c])
        if f < 0:  # if no flag is inputted, check neighbors for flags
            for n in self.mamonoGame.neighbors(r, c):
                if self.isNum(self.mamonoSolverBoard[r][c]) and tuple(n) in self.subtractedMonsters.keys():
                    # print("val: " + self.mamonoSolverBoard.monster_val[n[0]][n[1]]
                    self.mamonoSolverBoard[r][c] += int(self.mamonoSolverBoard[n[0]][n[1]])







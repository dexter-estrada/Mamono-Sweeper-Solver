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
            self.mamonoSolverBoard = copy.deepcopy(self.mamonoGame.monster_val)

        counter = 0
        while loop:
            counter += 1

            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    game_value = self.mamonoGame.monster_val[r][c]
                    solver_value = self.mamonoSolverBoard[r][c]
                    if self.isSolverDead():
                        counter = 1000
                        return None
                    if "F" in str(solver_value):
                        print("flagVAL" + str(solver_value[1]))
                        if self.mamonoGame.lvl >= int(solver_value[1]):
                            self.solverInput(r, c)
                            solver_value = self.mamonoSolverBoard[r][c]

                    if solver_value == 0 and not self.isNeighborsCleared(r, c):
                        self.clearNeighbors(r, c)
                    elif not self.isNum(game_value) or not self.isNum(solver_value):
                        continue
                    elif self.mamonoGame.lvl >= int(solver_value) > 0 and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are greater to level
                        for n in self.mamonoGame.neighbors(r, c):
                            self.solverInput(n[0], n[1])
                    elif int(solver_value) < 0 and (r, c) not in self.subtractedMonsters.keys():  # if solver board has negative values, update solver neighbors
                        self.subtractedMonsters[(r, c)] = solver_value
                        self.monsterSubtraction(r, c)

                    elif int(solver_value) > 0 and self.isCorner(r, c):  # corner value, must flag
                        for n in self.mamonoGame.neighbors(r, c):
                            if self.mamonoSolverBoard[n[0]][n[1]] == ' ':
                                self.mamonoSolverBoard[n[0]][n[1]] = 'F' + str(solver_value)
                                self.monsterSubtraction(n[0], n[1])

            if counter <= 200:  # temporarily run loop 30 times
                print(self.subtractedMonsters)
                loop = False

        print("counter: " + str(counter))

    def isSolverDead(self):
        if self.mamonoGame.hp <= 0:
            print("Solver Died")
            return True
        else:
            return False

    def isCorner(self, r, c):
        count_blanks = 0
        is_corner = True
        for n in self.mamonoGame.neighbors(r, c):
            if count_blanks > 1:
                is_corner = False
                break
            if self.mamonoSolverBoard[n[0]][n[1]] == ' ':
                count_blanks += 1

        return is_corner

    # checks if given value is a number (includes negatives), only checks ' ' and 'f'
    def isNum(self, num):
        if str(num) == ' ':
            return False
        elif "F" in str(num):
            return False

        return True

    def monsterSubtraction(self, r, c):
        if "F" in str(self.mamonoSolverBoard[r][c]):
            monster = -1 * int(self.mamonoSolverBoard[r][c][1])
        else:
            monster = self.mamonoSolverBoard[r][c]

        for n in self.mamonoGame.neighbors(r, c):  # make neighbors subtract by solver value
            if self.isNum(self.mamonoSolverBoard[n[0]][n[1]]) and int(self.mamonoSolverBoard[n[0]][n[1]]) > 0:
                if int(self.mamonoSolverBoard[n[0]][n[1]]) + int(monster) > 0:
                    # print(self.mamonoSolverBoard[n[0]][n[1]])
                    self.mamonoSolverBoard[n[0]][n[1]] += int(monster)
                else:
                    self.mamonoSolverBoard[n[0]][n[1]] = 0

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
            if self.mamonoSolverBoard[n[0]][n[1]] == ' ' or ("F" in str(self.mamonoSolverBoard[n[0]][n[1]])):
                return False

        return True

    def clearNeighbors(self, r, c):
        for n in self.mamonoGame.neighbors(r, c):
            if self.mamonoSolverBoard[n[0]][n[1]] == ' ':
                self.solverInput(n[0], n[1])

    def solverInput(self, r, c):  # calls input from game on solver and regular board, checks for flagged monsters
        input_string = str(r) + " " + str(c)

        if self.mamonoSolverBoard[r][c] != ' ' and ("F" not in str(self.mamonoSolverBoard[r][c])):
            return None
        if ("F" in str(self.mamonoSolverBoard[r][c])) and (int(self.mamonoSolverBoard[r][c][1]) > self.mamonoGame.lvl):
            return None
        self.mamonoGame.input(input_string)
        self.mamonoSolverBoard[r][c] = self.mamonoGame.monster_val[r][c]  # line not fixed for flag input
        # print(self.mamonoGame.monster_val[r][c])
        if int(self.mamonoSolverBoard[r][c]) < 0:
            return None
        for n in self.mamonoGame.neighbors(r, c):
            if self.isNum(self.mamonoSolverBoard[r][c]) and tuple(n) in self.subtractedMonsters.keys():
                # print("val: " + str(self.mamonoSolverBoard[n[0]][n[1]]))
                self.mamonoSolverBoard[r][c] += int(self.mamonoSolverBoard[n[0]][n[1]])







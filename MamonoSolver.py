from MamonoSweeperGame import MamonoSweeper
import copy
import random

class MamonoSolver:
    def __init__(self, mamonoGame):
        self.mamonoGame = mamonoGame
        self.mamonoSolverBoard = [[' ' for y in range(self.mamonoGame.board_size)] for x in range(self.mamonoGame.board_size)]
        self.subtractedMonsters = dict()  # Key = (row, col): value = monster level (negative)
        self.solver_stuck = True
        self.level_died = 0
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
            solver_stuck = True
            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    game_value = self.mamonoGame.monster_val[r][c]
                    solver_value = self.mamonoSolverBoard[r][c]
                    if self.isSolverDead():
                        return -1
                    if self.mamonoGame.lvl == 5:
                        self.levelClear()
                        break
                    if "F" in str(solver_value):  # clears flag if level is greater than flag
                        if self.mamonoGame.lvl >= int(solver_value[1]):
                            self.solverInput(r, c)
                            solver_value = self.mamonoSolverBoard[r][c]

                    if solver_value == 0 and not self.isNeighborsCleared(r, c):  # clears 0s and neighbors of 0s on board
                        self.clearNeighbors(r, c)
                        if self.mamonoGame.monster_val[r][c] == ' ' or "F" in str(self.mamonoSolverBoard[r][c]):
                            self.solverInput(r, c)

                    elif not self.isNum(game_value) or not self.isNum(solver_value):  # ignores ' ' and Flags
                        continue

                    elif self.mamonoGame.lvl >= int(solver_value) > 0 and not self.isNeighborsCleared(r, c):  # clears neighbors of values that are <= level
                        for n in self.mamonoGame.neighbors(r, c):
                            self.solverInput(n[0], n[1])
                        self.solver_stuck = False

                    elif int(solver_value) < 0 and (r, c) not in self.subtractedMonsters.keys():  # if solver board has negative values, update solver neighbors
                        self.monsterSubtraction(r, c)

                    elif int(solver_value) > 0 and self.isCorner(r, c):  # corner value, must flag
                        self.solver_stuck = False
                        for n in self.mamonoGame.neighbors(r, c):
                            if self.mamonoSolverBoard[n[0]][n[1]] == ' ':
                                self.mamonoSolverBoard[n[0]][n[1]] = 'F' + str(solver_value)
                                self.monsterSubtraction(n[0], n[1])


            if solver_stuck:
                empty_space = []  # tuples of empty spaces
                for r in range(self.mamonoGame.row_size):
                    for c in range(self.mamonoGame.col_size):
                        if self.mamonoSolverBoard[r][c] == ' ':
                            empty_space.append((r, c))  # appends where an empty space exists
                if len(empty_space) == 0:
                    break
                r = random.randrange(0, len(empty_space))
                self.solverInput(empty_space[r][0], empty_space[r][1])  # choose a random empty space and input it

            if counter == 50:  # run loop 50 times
                loop = False

        if not self.checkWin() and self.mamonoGame.hp > 0:
            for r in range(self.mamonoGame.row_size):
                for c in range(self.mamonoGame.col_size):
                    if self.mamonoGame.monster_val[r][c] == ' ':
                        self.mamonoGame.input(str(r) + " " + str(c))

        self.level_died = self.mamonoGame.lvl

        #  print("counter: " + str(counter))

    def isSolverDead(self):
        if self.mamonoGame.hp <= 0:
            # print("Solver Died")
            return True
        else:
            return False

    def levelClear(self):
        for r in range(self.mamonoGame.row_size):
            for c in range(self.mamonoGame.col_size):
                self.mamonoGame.input(str(r) + " " + str(c))

    def checkWin(self):
        return self.mamonoGame.player_won

    def isCorner(self, r, c):
        count_blanks = 0
        for n in self.mamonoGame.neighbors(r, c):
            if self.mamonoSolverBoard[n[0]][n[1]] == ' ' or "F" in str(self.mamonoSolverBoard[n[0]][n[1]]):
                count_blanks += 1
            if count_blanks > 1:
                return False

        return True

    # checks if given value is a number (includes negatives), only checks ' ' and 'f'
    def isNum(self, num):
        if str(num) == ' ':
            return False
        elif "F" in str(num):
            return False

        return True

    def monsterSubtraction(self, r, c):
        self.subtractedMonsters[(r, c)] = self.mamonoSolverBoard[r][c]

        if "F" in str(self.mamonoSolverBoard[r][c]):
            monster = -1 * int(self.mamonoSolverBoard[r][c][1])
        else:
            monster = self.mamonoSolverBoard[r][c]

        for n in self.mamonoGame.neighbors(r, c):  # make neighbors subtract by monster value
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
        rcounter = 0
        for row in self.mamonoSolverBoard:
            print(str(rcounter) + str(row))
            rcounter += 1

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

        if not (self.mamonoSolverBoard[r][c] == ' ' or ("F" in str(self.mamonoSolverBoard[r][c]))):
            return None
        if ("F" in str(self.mamonoSolverBoard[r][c])) and (int(self.mamonoSolverBoard[r][c][1]) > self.mamonoGame.lvl):
            return None
        self.solver_stuck = False
        self.mamonoGame.input(input_string)
        self.mamonoSolverBoard[r][c] = self.mamonoGame.monster_val[r][c]  # line not fixed for flag input
        # print(self.mamonoGame.monster_val[r][c])

        if int(self.mamonoSolverBoard[r][c]) < 0:  # if monster is inputted
            return None

        for n in self.mamonoGame.neighbors(r, c):  # checks if monsters/flags are nearby
            if self.isNum(self.mamonoSolverBoard[r][c]) and tuple(n) in self.subtractedMonsters.keys():
                if "F" in str(self.mamonoSolverBoard[n[0]][n[1]]):
                    monster = -1 * int(self.mamonoSolverBoard[n[0]][n[1]][1])
                else:
                    monster = int(self.mamonoSolverBoard[n[0]][n[1]])

                if int(self.mamonoSolverBoard[r][c]) + int(monster) > 0:
                    # print(self.mamonoSolverBoard[n[0]][n[1]])
                    self.mamonoSolverBoard[r][c] += int(monster)
                else:
                    self.mamonoSolverBoard[r][c] = 0







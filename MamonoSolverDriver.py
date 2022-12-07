from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver
from MamonoSolverRand import MamonoSolverRand


def ourSolver(amount_of_games=100):
    games_won = 0
    # Checks the win percentage of the board
    level_reached = [0, 0, 0, 0, 0]

    for i in range(0, amount_of_games):
        mamonoGameTemp = MamonoSweeper()
        mamonoSolverTemp = MamonoSolver(mamonoGameTemp)
        if mamonoSolverTemp.checkWin():
            games_won += 1
        level_reached[mamonoSolverTemp.mamonoGame.lvl - 1] += 1

    print("Winrate: ", (games_won / amount_of_games) * 100, "%, Out of ", amount_of_games, " games")
    print()
    print("Level Died At: ")
    level_percentage = 0
    for i in range(len(level_reached), 0, -1):
        print("Level " + str(i) + ": " + str(level_reached[i - 1]))
    print()
    print("Percentage of Level Reached: ")
    for i in range(len(level_reached), 0, -1):
        print("Level " + str(i) + ": ", end="")
        print(str(((level_reached[i - 1] + level_percentage) / amount_of_games) * 100) + "%")
        level_percentage += level_reached[i - 1]


def randomSolver(amount_of_games=100):
    games_won = 0
    # Checks the win percentage of the board
    level_reached = [0, 0, 0, 0, 0]

    for i in range(0, amount_of_games):
        mamonoGameTemp = MamonoSweeper()
        mamonoSolverRandom = MamonoSolverRand(mamonoGameTemp)
        if mamonoSolverRandom.checkWin():
            games_won += 1
        level_reached[mamonoSolverRandom.mamonoGame.lvl - 1] += 1

    print("Winrate: ", (games_won / amount_of_games) * 100, "%, Out of ", amount_of_games, " games")
    print()
    print("Level Died At: ")
    level_percentage = 0
    for i in range(len(level_reached), 0, -1):
        print("Level " + str(i) + ": " + str(level_reached[i - 1]))
    print()
    print("Percentage of Level Reached: ")
    for i in range(len(level_reached), 0, -1):
        print("Level " + str(i) + ": ", end="")
        print(str(((level_reached[i - 1] + level_percentage) / amount_of_games) * 100) + "%")
        level_percentage += level_reached[i - 1]


def main():
    # mamonoGameInstance = MamonoSweeper()
    # mamonoSolverInstance = MamonoSolver(mamonoGameInstance)
    # mamonoSolverRandom = MamonoSolverRand(mamonoGameInstance)

    # mamonoSolverInstance.printBoards()
    # mamonoSolverRandom.printBoards()

    print("Our Solver: ")
    ourSolver(10000)
    print()

    print("Random Solver")
    randomSolver(10000)
    print()

if __name__ == "__main__":
    main()



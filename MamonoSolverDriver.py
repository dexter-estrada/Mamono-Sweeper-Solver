from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver
from MamonoSolverRand import MamonoSolverRand


def main():
    mamonoGameInstance = MamonoSweeper()
    mamonoSolverInstance = MamonoSolver(mamonoGameInstance)
    # mamonoSolverRandom = MamonoSolverRand(mamonoGameInstance)

    mamonoSolverInstance.printBoards()
    # mamonoSolverRandom.printBoards()

    games_won = 0
    # Checks the win percentage of the board
    level_reached = [0, 0, 0, 0, 0]
    amount_of_games = 100

    for i in range(0, amount_of_games):
        mamonoGameTemp = MamonoSweeper()
        mamonoSolverTemp = MamonoSolver(mamonoGameTemp)
        if mamonoSolverTemp.checkWin():
            games_won += 1
        level_reached[mamonoSolverTemp.level_died-1] += 1

    print("Winrate: %", (games_won/amount_of_games) * 100, ", Out of ", amount_of_games, " games")

    print("Level Reached:")
    for i in range(len(level_reached)):
        print("Level " + str(i+1) + ": " + str(level_reached[i]))


if __name__ == "__main__":
    main()

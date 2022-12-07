from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver
from MamonoSolverRand import MamonoSolverRand


def main():
    mamonoGameInstance = MamonoSweeper()
    mamonoSolverInstance = MamonoSolver(mamonoGameInstance)
    mamonoSolverRandom = MamonoSolverRand(mamonoGameInstance)

    mamonoSolverInstance.printBoards()
    mamonoSolverRandom.printBoards()

    gamesWon = 0
    # Checks the win percentage of the board
    for i in range(0, 100):
        mamonoGameTemp = MamonoSweeper()
        mamonoSolverTemp = MamonoSolver(mamonoGameTemp)
        #if mamonoSolverTemp.checkWin():
            #gamesWon += 0
    print("Winrate: ", gamesWon, "/", 100)
    
if __name__ == "__main__":
    main()

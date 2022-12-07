from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver
from MamonoSolver2 import MamonoSolver2


def main():
    mamonoGameInstance = MamonoSweeper()
    #mamonoSolverInstance = MamonoSolver(mamonoGameInstance)
    mamonoSolverInstance2 = MamonoSolver2(mamonoGameInstance)

    #mamonoSolverInstance.printBoards()
    mamonoSolverInstance2.printBoards()


if __name__ == "__main__":
    main()

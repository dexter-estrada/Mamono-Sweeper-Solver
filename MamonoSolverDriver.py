from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver


def main():
    mamonoGameInstance = MamonoSweeper()
    mamonoSolverInstance = MamonoSolver(mamonoGameInstance)

    mamonoSolverInstance.printBoards()


if __name__ == "__main__":
    main()

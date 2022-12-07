from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver
from MamonoSolverRand import MamonoSolverRand


def main():
    mamonoGameInstance = MamonoSweeper()
    #mamonoSolverInstance = MamonoSolver(mamonoGameInstance)
    mamonoSolverInstance2 = MamonoSolverRand(mamonoGameInstance)

    #mamonoSolverInstance.printBoards()
    mamonoSolverInstance2.printBoards()


if __name__ == "__main__":
    main()

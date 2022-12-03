from MamonoSweeperGame import MamonoSweeper
from MamonoSolver import MamonoSolver


def main():
    mamonoGameInstance = MamonoSweeper()
    #mamonoSolverInstance = MamonoSolver(mamonoGameInstance)

    #mamonoSolverInstance.printBoards()
    mamonoGameInstance.print_board()
    #mamonoGameInstance.print_solution()


if __name__ == "__main__":
    main()
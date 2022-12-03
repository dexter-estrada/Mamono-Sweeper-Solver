import random   # For generating game
from colorama import Fore, Back, Style, init

class MamonoSweeper:
    def __init__(self):
        # Grid size
        self.row_size = 16
        self.col_size = 16
        # Grid size
        self.board_size = 16
        # Number of Monsters per level
        self.monster_num = [10, 8, 6, 4, 2]
        # Health Points
        self.hp = 10
        # Player Level
        self.lvl = 1
        # Experience Points
        self.exp = 0
        # Level up
        self.next = [7, 20, 50, 82]
        # Monster Experience Gain
        self.exp_gain = [1, 2, 4, 10, 100]
        # Damage taken
        #mon_dmg = [1, 2, 3, 4, 10]

        # The monster values of the grid
        self.numbers = [[0 for y in range(self.board_size)] for x in range(self.board_size)]
        # Values known to the player
        self.monster_val = [[' ' for y in range(self.board_size)] for x in range(self.board_size)]
        # User set flags
        self.flags = []
        # Uncovered tiles
        self.visible = []

        self.setup()


    # Prints the Mamono Sweeper board
    def print_board(self):

        print()
        print("\t\t\tMamono Sweeper")

        st = "   "
        for i in range(self.row_size):
            st = st + "     " + str(chr(i + 65))
        print(st)   
    
        for r in range(self.col_size):
            st = "     "
            if r == 0:
                for col in range(self.col_size):
                    st = st + "______" 
                print(st)
    
            st = "     "
            for col in range(self.col_size):
                st = st + "|     "
            print(st + "|")
            
            st = "  " + str(chr(r + 65)) + "  "
            for col in range(self.col_size):
                st = st + "|  " + str(self.monster_val[r][col]) + "  "
            print(st + "|") 
    
            st = "     "
            for col in range(self.col_size):
                st = st + "|_____"
            print(st + '|')
        print()

    # Print the solution
    def print_solution(self):
        print(Back.BLACK)
        print(Fore.WHITE)
        print("\t\t\tMamono Sweeper")

        st = "   "
        for i in range(self.row_size):
            st = st + "     " + str(chr(i + 65))
        print(st)   
    
        for r in range(self.col_size):
            st = "     "
            if r == 0:
                for col in range(self.col_size):
                    st = st + "______" 
                print(st)
    
            st = "     "
            for col in range(self.col_size):
                st = st + "|     "
            print(st + "|")

            st = "  " + str(chr(r + 65)) + "  "
            print(st, end="")
            for col in range(self.col_size):
                print("|  ", end="")
                if self.numbers[r][col] < 0:  # if it is a monster, color it red
                    if self.numbers[r][col] == -1:
                        color = Fore.CYAN
                    elif self.numbers[r][col] == -2:
                        color = Fore.RED
                    elif self.numbers[r][col] == -3:
                        color = Fore.MAGENTA
                    elif self.numbers[r][col] == -4:
                        color = Fore.YELLOW
                    elif self.numbers[r][col] == -5:
                        color = Fore.LIGHTGREEN_EX
                    else:
                        print("ERROR: INCORRECT ENEMY NUMBER")
                        color = Fore.RED
                    print(color + str(-self.numbers[r][col]), end="")
                elif self.numbers[r][col] == 0:
                    print(" ", end="")
                else:
                    print(Fore.LIGHTWHITE_EX + str(self.numbers[r][col]), end="")
                print(Fore.WHITE, end="")
                print(Back.BLACK, end="")
                print("  ", end="")
            print("|")
    
            st = "     "
            for col in range(self.col_size):
                st = st + "|_____"
            print(st + '|')
        print()

    # Places the monsters on the field
    def set_monsters(self):
        for mons in range(len(self.monster_num)):
            # Tracks number of monsters of a level
            count = 0
            mons_level = -1 * (mons + 1)  # Represents the monster's level
            while count < self.monster_num[mons]:
                # Generating random
                row = random.randint(0, self.row_size-1)
                col = random.randint(0, self.col_size-1)

                # Place monster
                if self.numbers[row][col] > -1:
                    count = count + 1
                    self.numbers[row][col] = mons_level

    # Sets the apparent value of adjacent monsters
    def set_values(self):
        for row in range(self.row_size):
            for col in range(self.col_size):
                # Skips tiles with monsters
                if self.numbers[row][col] < 0:
                    continue

                # Check up  
                if row > 0 and self.numbers[row-1][col] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row-1][col]
                # Check down    
                if row < self.row_size-1  and self.numbers[row+1][col] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row+1][col]
                # Check left
                if col > 0 and self.numbers[row][col-1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row][col-1]
                # Check right
                if col < self.col_size-1 and self.numbers[row][col+1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row][col+1]
                # Check top-left    
                if row > 0 and col > 0 and self.numbers[row-1][col-1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row-1][col-1]
                # Check top-right
                if row > 0 and col < self.col_size-1 and self.numbers[row-1][col+1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row-1][col+1]
                # Check below-left  
                if row < self.row_size-1 and col > 0 and self.numbers[row+1][col-1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row+1][col-1]
                # Check below-right
                if row < self.row_size-1 and col < self.col_size-1 and self.numbers[row+1][col+1] < 0:
                    self.numbers[row][col] = self.numbers[row][col] - self.numbers[row+1][col+1]

    # Recursively uncovers all adjacent 0s on the board
    def clear_zeros(self, row, col):
        if [row, col] not in self.visible:
            # Mark tile as visited
            self.visible.append([row, col])

            # If tile is 0
            if self.numbers[row][col] == 0:
                # Display it to the user
                self.monster_val[row][col] = self.numbers[row][col]

                # Recursively calls neighboring tiles
                if row > 0:
                    self.clear_zeros(row-1, col)
                if row < self.row_size-1:
                    self.clear_zeros(row+1, col)
                if col > 0:
                    self.clear_zeros(row, col-1)
                if col < self.col_size-1:
                    self.clear_zeros(row, col+1)    
                if row > 0 and col > 0:
                    self.clear_zeros(row-1, col-1)
                if row > 0 and col < self.col_size-1:
                    self.clear_zeros(row-1, col+1)
                if row < self.row_size-1 and col > 0:
                    self.clear_zeros(row+1, col-1)
                if row < self.row_size-1 and col < self.col_size-1:
                    self.clear_zeros(row+1, col+1)  

    # Returns the neighbors of a given [r, c] as a list of [r, c]
    def neighbors(self, r, c):
        nList = []

        for i in range(-1, 2):  # i = -1,0,1
            for j in range(-1, 2):  # i = -1,0,1
                if i == 0 and j == 0:
                    continue
                elif r + i < 0 or c + j < 0:
                    continue
                elif r + i >= self.row_size or c + j >= self.col_size:
                    continue
                else:
                    nList.append([r+i, c+j])

        return nList

    # Function to display the instructions
    def instructions(self):
        print("Instructions:")
        print("1. Enter row and column number to select a cell, Example \"2 3\"")
        print("2. In order to flag a monster, enter a number after row and column numbers, Example \"2 3 4\"")

    def check_win(self):
        pass
        #if len(self.visible) ==

    def input(self, inp):
        user_input = inp.split()

        r = ord(user_input[0]) - 65
        c = ord(user_input[1]) - 65

        if self.monster_val[r][c] == 0:
            self.clear_zeros(r, c)

        # self.monster_val[r][c] = self.numbers[r][c]

        # If landing on a monster, do battle calculation

        # If landing in a safe spot

        # If landing in a spot with an adjacent monster

        """
        # Standard input
        if len(user_input) == 2:
            # Sanitizing input
            try:
                test = list(map(int, user_input))
            except ValueError:
                print("Integer not found")
                self.instructions()

            # Get row and column numbers
            row = test[0]-1
            col = test[1]-1


            # Unflag the cell if already flagged
            if [row, col] in self.flags:
                self.flags.remove([row, col])




        # Flag input
        elif len(user_input) == 3:
            # Sanitizing input
            try:
                test = list(map(int, user_input))
            except ValueError:
                print("Integer not found")
                self.instructions()
            # Get row and column numbers
            row = test[0]-1
            col = test[1]-1



        # Checking if within the board
        if test[0] > self.board_size or test[0] < 0 or test[1] > self.board_size or test[1] < 0:
            print("Out of bounds")
            self.instructions()

        # Get row and column numbers
        row = test[0]-1
        col = test[1]-1

        # Check for game completion
        """

    def setup(self):
        # Monster setup
        self.set_monsters()

        # Setting hints
        self.set_values()

    """
    def main(self):
        # Monster setup
        self.set_monsters()

        # Setting hints
        self.set_values()

        # Display instructions
        self.instructions()

        # bool to check if game is finished
        game_finished = False

        # Game Loop
        while not game_finished:
            self.print_board()

            # User input
            user_input = input("Enter row number followed by space and column number. To flag a tile, enter the level number as the third input").split()

            # Standard input
            if len(user_input) == 2:

                # Sanitizing input
                try:
                    test = list(map(int, user_input))
                except ValueError:
                    print("Integer not found")
                    self.instructions()
                    continue

            # Flag input
            elif len(user_input) == 3:
                
                # Sanitizing input
                try:
                    test = list(map(int, user_input))
                except ValueError:
                    print("Integer not found")
                    self.instructions()
                    continue

                # Checking if within the board
                if test[0] > self.board_size or test[0] < 1 or test[1] > self.board_size or test[1] < 1:
                    print("Out of bounds")
                    self.instructions()
                    continue

                # Get row and column numbers
                row = test[0]-1
                col = test[1]-1

            else:
                print("Unexpected input!")
                self.instructions()
                continue



            # Checking if within the board
            if test[0] > self.board_size or test[0] < 1 or test[1] > self.board_size or test[1] < 1:
                print("Out of bounds")
                self.instructions()
                continue

            # Get row and column numbers
            row = test[0]-1
            col = test[1]-1

            # Unflag the cell if already flagged
            if [row, col] in self.flags:
                self.flags.remove([row, col])

            # If landing on a monster, do battle calculation

            # If landing in a safe spot

            # If landing in a spot with an adjacent monster

            # Check 
        
    if __name__ == "__main__":
        main()
    """
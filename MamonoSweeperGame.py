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
        # Number of Monsters alive
        self.monster_num_alive = []
        for x in self.monster_num:
            self.monster_num_alive.append(x)
        # Health Points
        self.hp = 10
        # Player Level
        self.lvl = 1
        # Experience Points
        self.exp = 0
        # Level up
        self.next_lvl = [7, 20, 50, 82, 0]
        # Monster Experience Gain
        self.exp_gain = [1, 2, 4, 8, 16]
        # Damage taken
        #mon_dmg = [1, 2, 3, 4, 10]

        # The monster values of the grid
        self.numbers = [[0 for y in range(self.board_size)] for x in range(self.board_size)]
        # Values known to the player
        self.monster_val = [[' ' for y in range(self.board_size)] for x in range(self.board_size)]
        # User set flags as a dictionary. Key = (row, col): value = flag level
        self.flags = {}
        # Uncovered tiles
        self.visible = []

        # Tracks if game is currently being played
        self.is_playing = False
        # Tracks if the player won
        self.player_won = False

        self.setup()


    # Prints the Mamono Sweeper board
    def print_board(self):
        print(Back.BLACK)
        print(Fore.WHITE)
        print(f"{'Mamono Sweeper' : ^100}")
        print(f"{'LV:' : >1}{self.lvl : <5}{'HP:' : >1}{self.hp : <5}{'EX:' : >1}{self.exp : <5}{'NE:' : >1}{self.next_lvl[self.lvl-1] : <5}")

        st = "      "
        for i in range(self.row_size):
            #st = st + "     " + str(chr(i + 65))
            st = st + f"{str(i): ^6}"
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

            #st = "  " + str(chr(r + 65)) + "  "
            print(f"{r: ^5}", end="")
            for col in range(self.col_size):
                print("|", end="")
                if self.monster_val[r][col] == ' ':
                    print(f"{' ': >3}", end="")
                elif (r, col) in self.flags:
                    print(Fore.GREEN + f"{self.monster_val[r][col]: >3}", end="")
                elif int(self.monster_val[r][col]) < 0:  # if it is a monster, color it red
                    if int(self.monster_val[r][col]) == -1:
                        color = Fore.CYAN
                    elif int(self.monster_val[r][col]) == -2:
                        color = Fore.RED
                    elif int(self.monster_val[r][col]) == -3:
                        color = Fore.MAGENTA
                    elif int(self.monster_val[r][col]) == -4:
                        color = Fore.YELLOW
                    elif int(self.monster_val[r][col]) == -5:
                        color = Fore.LIGHTGREEN_EX
                    else:
                        print("ERROR: INCORRECT ENEMY NUMBER")
                        color = Fore.RED
                    print(color + f"{str(-int(self.monster_val[r][col])): >3}", end="")
                else:
                    print(Fore.LIGHTWHITE_EX + f"{str(int(self.monster_val[r][col])): >3}", end="")
                print(Fore.WHITE, end="")
                print(Back.BLACK, end="")
                print("  ", end="")
            print("|")
    
            st = "     "
            for col in range(self.col_size):
                st = st + "|_____"
            print(st + '|')
        print()
        print(f"{'LV1:x' : <1}{self.monster_num_alive[0] : <5}{'LV2:x' : <1}{self.monster_num_alive[1] : <5}{'LV3:x' : <1}{self.monster_num_alive[2] : <5}{'LV4:x' : <1}{self.monster_num_alive[3] : <5}{'LV5:x' : <1}{self.monster_num_alive[4] : <5}")
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

            if self.numbers[row][col] == 0:     # If tile is 0
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
            elif self.numbers[row][col] > 0:    # If tile is a hint
                # Display it to the user
                self.monster_val[row][col] = self.numbers[row][col]
            elif self.numbers[row][col] < 0:    # If tile contains a monster
                # Check if flag prevents user from clicking
                if (row, col) in self.flags:
                    if self.lvl >= self.flags[(row, col)]:
                        # Do battle calculation
                        self.battle_calculation(row, col)
                        self.check_win()
                        # Display it to the user
                        self.monster_val[row][col] = self.numbers[row][col]
                        # Remove flag from flags
                        self.flags.pop((row, col))
                else:                               # No flag found
                    # Do battle calculation
                    self.battle_calculation(row, col)
                    self.check_win()
                    # Display it to the user
                    self.monster_val[row][col] = self.numbers[row][col]


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

    # Function to calculate damage taken by player
    def battle_calculation(self, row, col):
        mon_level = -self.numbers[row][col]
        level_difference = mon_level - self.lvl
        print("Player level: ", self.lvl, " Monster level: ", mon_level)
        dmg = 0
        if level_difference > 0:
            dmg = mon_level * level_difference      # Damage to player calculation: dmg = mon_level * level_difference
            self.hp -= dmg
        print("damage taken: ", dmg)

        if self.hp < 1:             # Player dies and game over
            self.is_playing = False
            #print("You died")
            self.player_won = False
        else:                       # Player lives and gains xp. xp gain calculation: 2^(mon's level)
            self.exp += 2**( -(self.numbers[row][col] + 1))
            while self.exp >= self.next_lvl[self.lvl - 1]:  # while exp is less than the level gain threshold
                # Level up
                self.lvl += 1
            # Subtracting 1 from monster_num_alive to track remaining monsters
            self.monster_num_alive[(-self.numbers[row][col]) - 1] -= 1

    # Function to modify flags on a square. 
    def modify_flag(self, row, col, flag_level):
        if flag_level > 0:                      # Placing a flag
            self.flags[(row, col)] = flag_level
            self.monster_val[row][col] = 'F' + str(flag_level)
        else:                                   # Removing a flag
            self.flags.pop((row, col))
            self.monster_val[row][col] = ' '

    # Function to display the instructions
    def instructions(self):
        print("Instructions:")
        print("1. Enter row and column number to select a cell, Example \"2 3\"")
        print("2. In order to flag a monster, enter a number after row and column numbers, Example \"2 3 4\"")

    # Checks if all elements of monster_num is 0
    def check_win(self):
        flag = True
        for x in self.monster_num_alive:
            if x > 0:
                flag = False
                continue
        self.player_won = flag
        #if len(self.visible) ==

    # Processes user input. Expects a string of 2 or 3 arguments
    def input(self, inp):
        user_input = inp.split()

        #r = ord(user_input[0]) - 65
        #c = ord(user_input[1]) - 65

        if len(user_input) == 2:    # User clears a square
            r = int(user_input[0])
            c = int(user_input[1])
            self.clear_zeros(r, c)

        elif len(user_input) == 3:  # User flags a square
            r = int(user_input[0])
            c = int(user_input[1])
            f = int(user_input[2])
            self.modify_flag(r, c, f)

        # If landing in a spot without a monster
        #if self.numbers[r][c] == 0:

        # If landing on a monster, do battle calculation
        #self.battle_calculation(r, c)

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
        
        # Resetting endgame tracker
        self.monster_num_alive = []
        for x in self.monster_num:
            self.monster_num_alive.append(x)
        self.is_playing = True
        self.player_won = False

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
        
    """
if __name__ == "__main__":
    game = MamonoSweeper()
    # Display instructions
    game.instructions()
    while game.is_playing:
        game.print_board()
        # User input
        user_input = input("Enter row number followed by space and column number. To flag a tile, enter the level number as the third input: ")
        # Does action in game
        game.input(user_input)

    if game.player_won:
        print("You Win!")
    else:
        print("You Died!")
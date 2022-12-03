import random   # For generating game

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
        self.exp_gain = [1, 2, 4, ]
        # Damage taken
        #mon_dmg = [1, 2, 3, 4, 10]

        # The monster values of the grid
        self.numbers = [[0 for y in range(self.board_size)] for x in range(self.board_size)]
        # Values known to the player
        self.monster_val = [[' ' for y in range(self.board_size)] for x in range(self.board_size)]
        # User set flags
        self.flags = []
        # Selected flags
        self.vis = []


    # Prints the Mamono Sweeper board
    def print_board(self):

        print()
        print("\t\t\tMamono Sweeper")

        st = "   "
        for i in range(self.row_size):
            st = st + "     " + str(i + 1)
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
            
            st = "  " + str(r + 1) + "  "
            for col in range(self.col_size):
                st = st + "|  " + str(self.monster_val[r][col]) + "  "
            print(st + "|") 
    
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
            mons_level = -1 * (mons + 1) # Represents the monster's level
            while count < self.monster_num[mons]:
                # Generating random
                row = random.randint(0, self.row_size)
                col = random.randint(0, self.col_size)

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


    # Returns the neighbors of a given [r, c] as a list of [r, c]
    def neighbors(self, r, c):
        nList = []

        for i in range(-1,2):  # i = -1,0,1
            for j in range(-1,2):  # i = -1,0,1
                if i == 0 and j == 0:
                    continue
                elif r + i < 0 or c + j < 0:
                    continue
                elif r + i >= self.row_size or c + j >= self.col_size:
                    continue
                else:
                    nList.append([r+i, c+j])

        return nList



    def input(self, inp):


    def main(self):
        # Monster setup
        self.set_monsters()

        # Setting hints
        set_values()

        # Display instructions
        instructions()

        # bool to check if game is finished
        game_finished = False

        # Game Loop
        while not game_finished:
            print_board()

            # User input
            user_input = input("Enter row number followed by space and column number. To flag a tile, enter the level number as the third input").split()

            # Standard input
            if len(user_input) == 2:

                # Sanitizing input
                try:
                    test = list(map(int, user_input))
                except ValueError:
                    print("Integer not found")
                    instructions()
                    continue

            # Flag input
            elif len(user_input) == 3:
                
                # Sanitizing input
                try:
                    test = list(map(int, user_input))
                except ValueError:
                    print("Integer not found")
                    instructions()
                    continue

                # Checking if within the board
                if test[0] > self.board_size or test[0] < 1 or test[1] > self.board_size or test[1] < 1:
                    print("Out of bounds")
                    instructions()
                    continue

                # Get row and column numbers
                row = test[0]-1
                col = test[1]-1

            else:
                print("Unexpected input!")
                instructions()
                continue



            # Checking if within the board
            if test[0] > self.board_size or test[0] < 1 or test[1] > self.board_size or test[1] < 1:
                print("Out of bounds")
                instructions()
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
import random   # For generating game


# Prints the Mamono Sweeper board
def print_board():
    global monster_values
    global board_size

    print()
    print("\t\t\tMamono Sweeper")

    st = "   "
    for i in range(board_size):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(board_size):
        st = "     "
        if r == 0:
            for col in range(board_size):
                st = st + "______" 
            print(st)
 
        st = "     "
        for col in range(board_size):
            st = st + "|     "
        print(st + "|")
         
        st = "  " + str(r + 1) + "  "
        for col in range(board_size):
            st = st + "|  " + str(monster_val[r][col]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(board_size):
            st = st + "|_____"
        print(st + '|')
 
    print()


if __name__ == "__main__":
    # Grid size
    board_size = 16
    # Number of Monsters per level
    monster_num = [10, 8, 6, 4, 2]

    # Health Points
    hp = 10
    # Player Level
    lvl = 1
    # Experience Points
    exp = 0
    # Level up
    next = [7, 20, 50, 82]
    # Monster Experience Gain
    exp_gain = [1, 2, 4, ]
    # Damage taken
    #mon_dmg = [1, 2, 3, 4, 10]

    # The monster values of the grid
    numbers = [[0 for y in range(board_size)] for x in range(board_size)]
    # Values known to the player
    monster_val = [[' ' for y in range(board_size)] for x in range(board_size)]
    # User set flags
    flags = []

    # Monster setup
    set_monsters()

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
            if test[0] > board_size or test[0] < 1 or test[1] > board_size or test[1] < 1:
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
        if test[0] > board_size or test[0] < 1 or test[1] > board_size or test[1] < 1:
            print("Out of bounds")
            instructions()
            continue

        # Get row and column numbers
        row = test[0]-1
        col = test[1]-1

        # Unflag the cell if already flagged
        if [row, col] in flags:
            flags.remove([row, col])

        # If landing on a 
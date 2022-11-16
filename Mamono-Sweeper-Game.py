from tkinter import *                           # For gui
from tkinter import messagebox as tkMessageBox  # For messages
from collections import deque                   # For lists
import random                                   # For generating game
import time                                     # For tracking time spent playing the game
from datetime import time, date, datetime

class MamonoSweeperGame:

    def __init__(self, tk):
        self.tk = tk


def main():
    # create window
    window = Tk()
    # create title
    window.title("Mamono Sweeper")
    # display to screen
    window.geometry('240x160')
    # run loop
    window.mainloop()


if __name__ == "__main__":
    main()
import tkinter as tki
from board import Board
from game_gui import GameGui

def run_boggle_game():
    root = tki.Tk()
    root.title("boggle game")

    # create logical board
    board = Board()

    # create GUI
    gui = GameGui(root, board)
    board.set_gui(gui)

    root.mainloop()


if __name__ == '__main__':
    run_boggle_game()
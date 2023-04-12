import tkinter as tki
from board import Board



class BoardUI:
    """
    creates the graphic board for the game
    """
    def __init__(self, parent, board Board, label_to_destroy=None):
        """
        :param parent: the root (TK)
        :param board: board for the game
        :param label_to_destroy: destroy old board label when starts a new game
        """
        self._board = board
        if label_to_destroy:
            label_to_destroy.destroy()
        self.letter_frame = tki.Frame(parent)
        self.letter_frame.grid(row=1, column=0)
        self._buttons = {}
        self.create_buttons()

    def create_buttons(self):
        """
        create the gui buttons for the game
        """
        self._buttons = {}
        board_array = self._board.get_board_values()
        for row_idx in range(len(board_array)):
            for column_idx in range(len(board_array)):
                button = tki.Button(self.letter_frame, font=('Courier', 20),
                                    text=board_array[row_idx][column_idx])
                button.bind("<Button-1>", self.button_pressed)
                self._buttons[button] = (row_idx, column_idx)
                button.grid(row=row_idx, column=column_idx)

    def button_pressed(self, event):
        """
        save location of a button that was pressed
        """
        position = self._buttons[event.widget]
        if self._board.is_valid_selection(position):
            event.widget["state"] = ['disabled']
            event.widget.config(relief=tki.SUNKEN, background='light green', foreground='black')
        self._board.add_position(position)

    def clear_location_list(self):
        """
        clears the list of the pressed buttons when the user click on enter/clear/new game
        :return:
        """
        self._board.clear_location_list()
        for button in self._buttons:
            button["state"] = ['active']
            button.config(relief=tki.RAISED, background='white', foreground='black')

    def destroy_old_board_label(self):
        """
        delete old board when a new game starts
        """
        self.letter_frame.grid_forget()


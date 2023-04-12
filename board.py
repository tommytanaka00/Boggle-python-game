import boggle_board_randomizer


class Board:
    """
    the logic for the board
    """
    def __init__(self):
        self._board = None
        self._location_list = []
        self._gui = None

    def new_game(self):
        """
        get a random board from boggle_board_randomizer
        :return:
        """
        self._board = boggle_board_randomizer.randomize_board()

    def get_board_values(self):
        """
        :return: board, an array of arrays
        """
        return self._board

    def set_gui(self, gui):
        """
        set the gui for the game
        :param gui:
        :return:
        """
        self._gui = gui

    def is_valid_selection(self, position):
        """

        :param position: tuple of ints = position on board
        :return:
        """
        if position in self._location_list:
            return False
        if not len(self._location_list):
            return True
        last_position = self._location_list[-1]
        if abs(position[0] - last_position[0]) > 1:
            return False
        if abs(position[1] - last_position[1]) > 1:
            return False
        return True

    def add_position(self, position):
        """
        add position to a list
        :param position: tuple of ints = position on board
        :return:
        """
        if self.is_valid_selection(position):
            self._location_list.append(position)
            self._gui.update_word(self._board[position[0]][position[1]])

    def create_current_word(self, location_list):
        """
        takes position on the board and turn it to the current word the user typed
        :param location_list: list of all positions
        :return:
        """
        current_word = ""
        for elem in location_list:
            current_word += self._board[elem[0]][elem[1]]
        return current_word

    def is_word_valid(self, current_word, word_set):
        """
        check if a word exist in the game
        :param current_word: the word the user try to guess
        :param word_set: all valid words
        :return:
        """
        if current_word in word_set:
            return True

    def clear_location_list(self):
        """
        :return: an empty list
        """
        self._location_list = []

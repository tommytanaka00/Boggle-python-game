import tkinter as tki
from board_ui import BoardUI
from board import Board
import game
from timer import Timer
from tkinter import messagebox
import sys


class GameGui:

    TIME_FOR_GAME = 180

    def __init__(self, root, board: Board):
        self.root = root
        self.game = game.Game()
        self.cur_word = ""
        self.guessed_word_lst = self.game.get_word_list()

        self.score_label = None
        self.word_label = None
        self.score_list_label = None
        self.timer_label = None
        self.start_game_button = None
        self._board = board

        self.display_label = tki.Label(root, text="Boggle 4x4 \n(by Tom Tanaka and Yahel Reiss)", font=('Courier', 10), foreground='red')
        self.display_label.grid(row=0, column=0)

        self.before_game_label = tki.Label(root, text="Press 'new game' to start\n Are you ready?", font=('Courier', 13), background='light blue')
        self.before_game_label.grid(row=1, column=0)

        self.create_cur_word_and_wrdlst(self.cur_word, self.guessed_word_lst)
        self.create_enter_clear_button()
        self.create_score_and_timer(self.game.get_score(), 0)
        self.timer = Timer(self.root, self.timer_label, 180, self._time_over)
        self._is_game_running = False

    def _time_over(self):

        end_of_game_box = tki.messagebox.askyesno("Game over!", "Your final score was " + str(self.game.get_score()) +
                                                 '.\n Do you want to play again?')
        if end_of_game_box:
            self.new_game()
        else:
            sys.exit(0)
        self._is_game_running = False

    def new_game(self):
        """
        start a new boggle game after pressing the start_button
        :return:
        """
        self._board.new_game()
        self._board.clear_location_list()
        if self._is_game_running:
            self.reset()
        self.clear()
        self.timer.start()
        self._is_game_running = True
        self._board_ui = BoardUI(self.root, self._board, self.before_game_label)

    def clear(self):
        """
        clears the current word so that the user can start again
        :return:
        """
        if not self._is_game_running:
            return
        self.word_label.configure(text="word:")
        self.cur_word = ""
        self._board_ui.clear_location_list()

    def create_enter_clear_button(self):
        """
        create the gui for the buttons: enter, clear and star new game
        :return:
        """
        enter_frame = tki.Frame(self.root)
        enter_frame.grid(row=10, column=0)

        enter_button = tki.Button(enter_frame, text="ENTER", font=('Courier', 18), background='green', command=self.enter)
        enter_button.grid(column=0, row=0)

        clear_button = tki.Button(enter_frame, text="CLEAR", font=('Courier', 18), background='red', command=self.clear)
        clear_button.grid(column=1, row=0)

        start_button = tki.Button(self.root, text="NEW GAME", font=('Courier', 10), command=self.new_game)
        start_button.grid(column=3, row=0)

    def create_cur_word_and_wrdlst(self, cur_word, word_list):
        cur_word_and_word_list_frame = tki.Frame(self.root)
        cur_word_and_word_list_frame.grid(row=1, column=1)

        word = tki.Label(cur_word_and_word_list_frame, text="word: " + cur_word, font=('Courier', 10))
        word.grid(row=0, column=0)
        self.word_label = word

        word_list_title = tki.Label(cur_word_and_word_list_frame, text="Word list:", font=('Courier', 10))
        word_list_title.grid(row=1, column=0)

        word_list_scroll_bar = tki.Scrollbar(cur_word_and_word_list_frame)
        word_list_scroll_bar.grid(row=2, column=1)

        scroll_list = tki.Listbox(cur_word_and_word_list_frame, yscrollcommand=word_list_scroll_bar.set)
        self.score_list_label = scroll_list
        for word1 in word_list:
            scroll_list.insert(tki.END, word1)
        scroll_list.grid(row=2, column=0)

        word_list_scroll_bar.config(command=scroll_list.yview)

    def update_word(self, letter):
        if not self._is_game_running:
            return
        self.cur_word += letter
        self.word_label.configure(text='word: ' + self.cur_word)

    def create_score_and_timer(self, score, timer):
        score_and_timer_frame = tki.Frame(self.root)
        score_and_timer_frame.grid(row=1, column=2)

        score_label = tki.Label(score_and_timer_frame, text="score: " + str(score), font=('Courier', 10))
        score_label.grid(row=0)
        self.score_label = score_label

        timer_label = tki.Label(score_and_timer_frame, font=('Courier', 10))
        timer_label.grid(row=1)
        self.timer_label = timer_label

    def enter(self):
        if not self._is_game_running:
            # self.game.reset_words_list()
            return
        if self.cur_word:
            success = self.game.put_in_list_and_add_score(self.cur_word)  # returns Bool
            if success:
                self.score_label.configure(text="score: " + str(self.game.get_score()))
                self.score_list_label.insert(tki.END, self.cur_word)
        self.clear()

    def reset(self):
        self.reset_score()
        self.reset_word_list()
        self.delete_board()

    def reset_score(self):
        self.game.reset_score()
        self.score_label.configure(text="score: " + str(self.game.get_score()))

    def reset_word_list(self):
        self.game.reset_words_list()
        self.score_list_label.delete(0, tki.END)

    def delete_board(self):
        self._board_ui.destroy_old_board_label()

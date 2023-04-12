import tkinter as tki

class Timer:

    def __init__(self, root, label, duration, expired_func):
        self._root = root
        self._label = label
        self._origi_label_bg = self._label.cget('bg')
        self._duration = duration
        self._time_left = None
        self._expired_func = expired_func
        self._is_active = False
        self._ignore_timeout = False

    def start(self):
        self._time_left = self._duration
        if self._is_active:
            self._ignore_timeout = True
        self.update_clock(True)

    def _update_label(self):
        minute = self._time_left // 60
        second = self._time_left % 60
        if second // 10 == 0:
            self._label.configure(text='time left: ' + str(minute) + ':0' + str(second))
        else:
            self._label.configure(text='time left: ' + str(minute) + ':' + str(second))
        if self._time_left <= 15:
            self._label.config(background="#ff0000" if self._time_left % 2 else "#808080")
        else:
            self._label.config(background=self._origi_label_bg)

    def update_clock(self, force = False):
        """
        updates the timer and creates the label
        """
        if self._ignore_timeout and not force:
            self._ignore_timeout = False
            return
        self._update_label()
        self._time_left -= 1
        if self._time_left >= 0:
            self._root.after(1000, self.update_clock)
            self._is_active = True
        else:
            self._is_active = False
            self._expired_func()



    def change_color(self):
        """
        changes the background of the timer
        :return:
        """
        current_color = self._label.cget("background")
        next_color = "SystemButtonFace" if current_color == "OrangeRed2" else "OrangeRed2"
        self._label.config(background=next_color)

    def get_now(self):
        """
        return how much time left on the timer
        :return: time_left
        """
        return self._time_left



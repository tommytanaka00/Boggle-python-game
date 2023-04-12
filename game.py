

class Game:

    def __init__(self):
        self.WORD_SET = set()
        with open('boggle_dict.txt') as boggle_dict:
            for word in boggle_dict:
                self.WORD_SET.add(word.replace('\n', ''))
        self.word_list = []
        self.score = 0

    def check_if_word_exists(self, word):
        if word.upper() in self.WORD_SET:
            return True
        return False

    def put_in_list_and_add_score(self, word):
        """
        puts in list and adds score
        :param word:
        :return: Returns True if successful, False if not
        """
        if self.check_if_word_exists(word):
            if word.upper() not in self.word_list:
                self.word_list.append(word.upper())
                self.score += len(word) ** 2
                return True
        return False

    def reset_words_list(self):
        self.word_list = []

    def get_word_list(self):
        return self.word_list

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0
import pandas as pd

import src.utils.helper_functions as help
from src.constants import SKIP_WORDS_LIST


class Word:
    def __init__(self, original_word_from_language, original_word_to_language):
        self.original_word_from_language = original_word_from_language
        self.original_word_to_language = original_word_to_language
        self.correct_answer_from_language = help.clean_string(original_word_from_language)
        self.correct_answer_to_language = help.clean_string(original_word_to_language)

    def give_hint(self):
        """
        This function gives a hint based on the answer.
        All characters that aren't letters are shown in the hint.
        If the answer starts with a word for skip_words_list it is shown in the hint.
        The first letter is (after the word from skip_words_list) shown in the hint.
        All other letters are shown as dots.

        Examples:
        answer_string = "solution" --> hint = "s......."
        answer_string = "Hello everyone!" --> hint = "H.... ........!"
        answer_string = "¡Hola!" --> hint = '¡H...!"
        answer_string = "la tortuga" --> hint = "la t......"
        """

        hint = ""
        hint_index = 0  # the index of the character that should be given as hint

        # words from skiplist are shown in the hint
        first_word = self.correct_answer_to_language.lower().split(" ", 1)[0]
        if first_word in SKIP_WORDS_LIST:
            hint += first_word + " "  # add this word to the hint + a space
            hint_index = len(first_word) + 1

        # show the first letter
        for ch in self.correct_answer_to_language[hint_index:]:
            hint_index += 1
            if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
                hint += ch  # add the letter that gives the hint
                break
            else:
                hint += ch  # add the ch that isn't a letter

        # for all other characters; dots for letters, other characters are shown
        for ch in self.correct_answer_to_language[hint_index:]:
            if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
                hint += "."
            else:
                hint += ch

        return hint

    @staticmethod
    def create_word(from_language: str, to_language: str, word_info: pd.Series):
        return Word(word_info[from_language], word_info[to_language])

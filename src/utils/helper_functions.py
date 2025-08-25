import re


def clean_string(string1):
    """
    Removes unnecessary spaces and text in between the parentheses () and write in lowercase.
    """

    # Removing everything between parentheses using regex
    string1_without_parentheses = re.sub(r"\(.*?\)", "", string1)

    # Remove unnecessary spaces on beginning, end, and between words
    string1_cleaned = re.sub(r"\s+", " ", string1_without_parentheses.strip())

    return string1_cleaned.lower()


def give_hint(answer_string, skip_words_list):
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
    for word in skip_words_list:
        if answer_string.lower().startswith(word.strip() + " "):  # check if answer starts with this word
            hint += answer_string[: len(word) + 1]  # add this word to the hint
            hint_index = len(word) + 1
            break  # no need to check the other words in skip_words_list

    # show the first letter
    for ch in answer_string[hint_index:]:
        hint_index += 1
        if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
            hint += ch  # add the letter that gives the hint
            break
        else:
            hint += ch  # add the ch that isn't a letter

    # for all other characters; dots for letters, other characters are shown
    for ch in answer_string[hint_index:]:
        if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
            hint += "."
        else:
            hint += ch

    return hint

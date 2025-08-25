import src.utils.helper_functions as help

from src.words import Word


def test_clean_string_with_parentheses():
    assert help.clean_string("La tortuga (extra info)") == "La tortuga"


def test_clean_string_basic():
    assert help.clean_string("El perro corre rapido") == "El perro corre rapido"


def test_clean_string_multiple_spaces():
    assert help.clean_string("  El   gato   ") == "El gato"


def test_clean_string_empty():
    assert help.clean_string("") == ""


def test_clean_string_only_parentheses():
    assert help.clean_string("(hidden info)") == ""


def test_clean_string_trailing_spaces():
    assert help.clean_string("La casa (azul)   ") == "La casa"


def test_clean_string_no_closing_parenthesis():
    assert help.clean_string("Hola (mundo") == "Hola (mundo"


def test_give_hint_with_skip_word():
    test_word = Word("the bear", "el oso")
    hint = "el o.."
    assert test_word.give_hint() == hint


def test_give_hint_with_unnecessary_space():
    test_word = Word("el gato", "the cat ")
    hint = "the c.."
    assert test_word.give_hint() == hint


def test_give_hint_no_skip_words():
    test_word = Word("to work", "trabajar")
    hint = "t......."
    assert test_word.give_hint() == hint


def test_give_hint_multiple_words():
    test_word = Word("Hallo allemaal", "Hello everyone")
    hint = "H.... ........"
    assert test_word.give_hint() == hint


def test_give_hint_exclamation_marks():
    test_word = Word("Hallo!", "¡Hola!")
    hint = "¡H...!"
    assert test_word.give_hint() == hint

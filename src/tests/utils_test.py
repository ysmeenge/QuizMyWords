import src.utils.helper_functions as help

mock_skip_list = ["to", "a", "an", "la", "el", "un", "una", "een", "het", "de"]


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


def test_give_hint_no_skip_words():
    assert help.give_hint("trabajar", mock_skip_list) == "t......."


def test_give_hint_multiple_words():
    assert help.give_hint("Hello everyone", mock_skip_list) == "H.... ........"


def test_give_hint_with_skip_word():
    assert help.give_hint("el oso", mock_skip_list) == "el o.."


def test_give_hint_exclamation_marks():
    assert help.give_hint("¡Hola!", mock_skip_list) == "¡H...!"


def test_give_hint_empty_string():
    assert help.give_hint("", mock_skip_list) == ""

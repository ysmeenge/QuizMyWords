import src.utils.helper_functions as help


# Test cases for clean_string
def test_clean_string_basic():
    assert help.clean_string("La tortuga (extra info)") == "La tortuga"


def test_clean_string_no_parentheses():
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

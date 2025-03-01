import re


def clean_string(string1):
    """
    Removes unnecessary spaces and text in between the parentheses ().
    """

    # Removing everything between parentheses using regex
    string1_without_parentheses = re.sub(r"\(.*?\)", "", string1)

    # remove unnessary spaces on beginning and end and remove double spaces
    string1_cleaned = string1_without_parentheses.strip().replace("  ", " ")

    return string1_cleaned

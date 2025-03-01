import os
import pandas as pd


def ask_file_name():  # Note: future improvment -> error messages are delayed
    # Get all .csv files in the 'data' folder
    data_folder = "src\\data"
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

    # Check if there are CSV files available
    if not csv_files:
        print("No CSV files found in the 'data' folder.")
        return None

    # Show a numbered list of files
    print("Select a file to be quizzed on:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file}")

    # Get user choice
    while True:
        try:
            choice = int(input("Enter the number of the file: "))
            print("You entered: ", choice)
            if 1 <= choice <= len(csv_files):
                return csv_files[choice - 1]  # Return the selected file name
            else:
                print("\n ERROR: Invalid number. Please choose a number from the list.", flush=True)
                print()
        except ValueError:
            print("\n ERROR: Invalid input. Please enter a number.", flush=True)
            print()


def choose_language_order(word_list_df):

    language1 = word_list_df.columns[0]
    language2 = word_list_df.columns[1]

    language_options = ""  # lege string

    while language_options != "1" and language_options != "2":
        language_options = input(
            "Choose the direction you want to learn the language? \n"
            "1. {language1} -> {language2} \n"
            "2. {language2} -> {language1} \n"
            "Type 1 or 2. \n".format(language1=language1, language2=language2)
        )

        if language_options == "1":
            from_language = language1
            to_language = language2
        elif language_options == "2":
            from_language = language2
            to_language = language1
        else:
            print("You didn't answer correctly! Please try again!")

    print(f"Great! We will quiz words from {from_language} to {to_language}.\n")

    return (from_language, to_language)


def select_quiz_type():
    quiz_number = -1
    quiz_number = input(
        """What kind of quiz would you like to do?
    1. Flascards - Come up with the translation in your head. No grade is given.
    2. Quiz - Type in the answer. Each word is asked once.
    3. Repeated Quiz - Type in the answer. Repeated until correct.
    4. Multiple choice - Repeated until correct.
  Type in which quiz type you want (1,2,3,4): """
    )

    while quiz_number not in ("1", "2", "3", "4"):
        quiz_number = input("This input is incorrect. Please type in one of the following numbers (1, 2, 3, 4): ")
    quiz_number = int(quiz_number)

    # Select action for user
    if quiz_number == 1:
        action_string = "Type 'h' if you want a hint. \n Press ENTER when you have the word in your head.\n"
    elif quiz_number == 2 or quiz_number == 3:
        action_string = "Type 'h' if you want a hint. \n Type in your answer: \n"
    elif quiz_number == 4:
        action_string = "Type the number with the correct answer: \n"

    return quiz_number, action_string


def start_program():

    chosen_file_name = ask_file_name()

    word_list_df = pd.read_csv("src\\data\\" + chosen_file_name)

    from_language, to_language = choose_language_order(word_list_df)

    select_quiz_type()

    print(f"Let's START! We will quiz words from {from_language} to {to_language}.\n")

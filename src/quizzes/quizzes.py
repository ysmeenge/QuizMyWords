from random import choice
import numpy as np

import src.utils.helper_functions as help


def start_quiz(word_list_df, from_language, to_language, quiz_number, action_string, skip_words_list):
    nr_words_tested = 0
    nr_words_correct = 0
    test_file = word_list_df.copy()  # need a copy cause we don't want to change the orginal word_list_df

    while len(test_file) > 0:

        # Select the word to be translated
        row_index = choice(list(test_file.index))  # randomly choose row index from test_file
        translate_word = test_file[from_language][row_index]  # [column_name][row_index]
        correct_answer = test_file[to_language][row_index]  # [column_name][row_index]
        nr_words_tested += 1

        if quiz_number == 4:
            random_list = np.random.choice(
                word_list_df.drop([row_index]).index, 3, replace=False
            )  # randomly choice 3 indicex (excluding that of the correct answer)
            random_list = np.append(random_list, row_index)  # add the index of the correct answer
            np.random.shuffle(random_list)  # shuffle row_indices

            # update action string
            action_string = f"""The options are:
            1. {word_list_df[to_language][random_list[0]]}
            2. {word_list_df[to_language][random_list[1]]}
            3. {word_list_df[to_language][random_list[2]]}
            4. {word_list_df[to_language][random_list[3]]}
            Type the number with the correct answer: \n"""

        # Ask user for input
        user_input = input(
            f"""\n Can you translate '{translate_word}' to {to_language}?
            {action_string}"""
        )

        if quiz_number == 4:
            while user_input not in ("1", "2", "3", "4"):
                user_input = input("This input is incorrect. Please fill out one of the following integers: 1, 2, 3, 4.\n")
            user_input = int(user_input)
            user_input = word_list_df[to_language][random_list[user_input - 1]]  # find word corresponding to this input

        # Give hint if asked
        if user_input == "h":
            hint = help.give_hint(correct_answer, skip_words_list)
            user_input = input(f"The hint is: '{hint}'. Please try again: \n")

        # check if correct answer is typed in
        if user_input == help.clean_string(correct_answer):
            print("This answer is CORRECT!\n")
            nr_words_correct += 1
        else:
            if user_input != help.clean_string(correct_answer) and quiz_number != 1:
                print("This answer is WRONG!")
            print(f"The correct answer is '{correct_answer}'.\n")

        # remove this row if answer is correct OR we only quiz each word once
        if quiz_number == 1 or quiz_number == 2 or user_input == help.clean_string(correct_answer):
            test_file.drop([row_index], inplace=True)

    print("YOU'VE FINISHED THE QUIZ!")
    if quiz_number in (2, 3, 4):
        grade = nr_words_correct / nr_words_tested * 10
        print(f"You're grade is: {grade:2.1f}")

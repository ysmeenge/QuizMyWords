import random


def start_quiz(word_list, to_language, quiz_number, action_string):
    nr_words_tested = 0
    nr_words_correct = 0
    test_word_list = word_list.copy()  # need a copy cause we don't want to change the orginal word_list

    while len(test_word_list) > 0:

        # Select the word to be translated
        chosen_word = random.choice(test_word_list)  # randomly choose row index from test_word_list
        nr_words_tested += 1

        if quiz_number == 4:
            word_list_copy = word_list.copy()
            word_list_copy.remove(chosen_word)  # chosen_word shouldn't be in the answers twice
            multiple_choice_options = random.sample(word_list_copy, 3)  # get 3 words randomly
            multiple_choice_options.append(chosen_word)  # add correct answer to options
            random.shuffle(multiple_choice_options)

            # update action string
            action_string = f"""The options are:
            1. {multiple_choice_options[0].correct_answer_to_language}
            2. {multiple_choice_options[1].correct_answer_to_language}
            3. {multiple_choice_options[2].correct_answer_to_language}
            4. {multiple_choice_options[3].correct_answer_to_language}
            Type the number with the correct answer: \n"""

        # Ask user for input
        user_input = input(
            f"""\n Can you translate '{chosen_word.original_word_from_language}' to {to_language}?
            {action_string}"""
        )

        if quiz_number == 4:
            while user_input not in ("1", "2", "3", "4"):
                user_input = input("This input is incorrect. Please fill out one of the following integers: 1, 2, 3, 4.\n")
            user_input = int(user_input)
            user_input = multiple_choice_options[user_input - 1]  # find word corresponding to this input

        # Give hint if asked
        if user_input == "h":
            hint = chosen_word.give_hint()
            user_input = input(f"The hint is: '{hint}'. Please try again: \n")

        is_answer_correct = user_input.lower() == chosen_word.correct_answer_to_language.lower()

        if is_answer_correct:
            print("This answer is CORRECT!\n")
            nr_words_correct += 1
        else:
            if quiz_number != 1:
                print("This answer is WRONG!")
            print(f"The correct answer is '{chosen_word.correct_answer_to_language}'.\n")

        # remove this row if answer is correct OR we only quiz each word once
        if quiz_number == 1 or quiz_number == 2 or is_answer_correct:
            test_word_list.remove(chosen_word)

    print("YOU'VE FINISHED THE QUIZ!")
    if quiz_number in (2, 3, 4):
        grade = nr_words_correct / nr_words_tested * 10
        print(f"You're grade is: {grade:2.1f}")

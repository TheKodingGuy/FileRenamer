from single_file_rename_mode import single_mode
from batch_file_rename_mode import batch_mode


def renamer():
    supported_responses = ['s', 'b']
    user_choice = 'unset input'

    while user_choice[0].lower() not in supported_responses:
        user_choice = input("Choose a rename mode batch (b) or single (s): ")
        if user_choice[0].lower() in supported_responses[0]:
            print("SINGLE MODE ON")
            single_mode()
        elif user_choice[0].lower() in supported_responses[1]:
            print("BATCH MODE ON")
            batch_mode()

        else:
            print("ERROR! Try again: ")

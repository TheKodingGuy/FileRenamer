from single_file_rename_mode import single_mode


def renamer():
    supported_responses = 's'
    user_choice = 'unset input'

    while user_choice[0].lower() not in supported_responses:
        user_choice = input("To start enter (s): ")
        if user_choice[0].lower() in supported_responses[0]:
            print("SINGLE MODE ON")
            single_mode()

        else:
            print("ERROR! Try again: ")

import os


def single_mode():
    es = 0
    for f in os.listdir():
        try:
            # Returns file name seperated from directory data and file extension
            original_ext = os.path.splitext(f)[1]

            file_basename = os.path.basename(f)

            # Prompts user to give a new file name
            user_input_file_name = input(
                f"For file > {file_basename} < pick a new file name: ")

            new_file_name = user_input_file_name + original_ext

            # Replaces old file name with user generated file name
            src = f
            dst = new_file_name

            os.rename(src, dst)

        except FileExistsError:
            print(src)
            print(dst)
            print("SAME NAME ERROR!")
        else:
            print(
                f"\nFile: {file_basename} has been renamed to {new_file_name}")
            es += 1

        if len(os.listdir()) == es:
            print("\nDONE\n")

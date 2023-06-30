import os
import shutil


def batch_mode():
    num = 1
    original_ext = []
    n = 0
    run = 'n'
    try:
        bf = os.listdir()

        for file_name in bf:
            original_ext.append(os.path.splitext(file_name)[1])

        while True:
            new_batch_file_name = input(
                "Choose a new file name for all files: ")
            print(
                f"What your files new name will look like: \n{new_batch_file_name}" + "01")
            print(
                "\nConfirm that this is what you want your files to be renamed too")
            confirm = input("(C) to confirm - (E) to enter a different name: ")
            if confirm == 'c':
                run = 'y'
                break
            elif confirm == 'e':
                continue

        if run == 'y':

            new_name = new_batch_file_name

            for f in os.listdir():
                src = f
                dst = new_name + str(num).zfill(2) + original_ext[n]

                os.rename(src, dst)
                num += 1
                n += 1

            for f in os.listdir():
                move_src = f
                move_dst = r'C:\Users\Example\Example\Example\File_Renamer\Files_To_Rename'
                # ^ ENTER THE NAME OF THE DIRECTORY WHERE YOU WOULD LIKE YOUR RENMAED FILES STORED

                shutil.move(move_src, move_dst)

    except FileExistsError:
        print(src)
        print(dst)
        print("SAME NAME ERROR!")
    else:
        for nf in os.listdir(move_dst):
            print(f"File: {nf} has been renamed")

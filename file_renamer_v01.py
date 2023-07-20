# RUN PROGRAM HERE

import os
from renamer import renamer

rename = r'C:\Users\Example\Example\Example\File_Renamer\Files_To_Rename'
# ^ ENTER THE NAME OF THE DIRECTORY WHERE THE FILES YOU WOULD LIKE TO RENAME ARE SORED HERE

os.chdir(rename)

try:
    renamer()
except IndexError:
    print("ERROR!")
    renamer()

"""
Entry point
"""

import os
import sys

# importing custom classes
import PassOne

# defining global variables
global SYMTAB, file_contents, program_name, start_address, line_address, begin
SYMTAB, file_contents, program_name, start_address, line_address, begin = {}, [], "", 0, 0, 0


def main():

    # inputting the source file
    source_file = input("Enter Source File(full path): ")
    if not os.path.exists(source_file):
        sys.exit("File does not exist.")

    # inputting ouput file name
    out_file_name = input("Enter Object Code File Name: ")
    out_file_name.replace(" ", "")

    SYMTAB, file_contents, program_name, start_address, line_address, begin = PassOne.pass_one(
        source_file)


# ----------------------- main -----------------------
if __name__ == "__main__":
    main()

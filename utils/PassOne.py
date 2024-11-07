"""
Performs Pass One functions to generate Symbol Table and reads every line
Also performs error checking, syntactical
"""

import re
import time
import sys

# importing custom classes
from Line import Line
import Helpers
import Opcodes

# contents after LINE_SIZE is considered as comments, thus ignored
global LINE_SIZE
LINE_SIZE: int = 40

# maximum availabel size
global MAX_SPACE
MAX_SPACE: int = 1048576

# symbol table
global SYMTAB
SYMTAB: dict = {}

# file contents
global file_contents
file_contents: list = []

# extract features from each line and return a Line object


def get_line(line: str):
    is_comment: bool = False
    executable_code: str = ""
    mnemonic: str = ""
    args: str = ""
    label: str = ""
    extended: bool = False

    # regex for comment or empty line matching
    match = re.match(r"(^\s*\.\s*(?P<comment>.*)?)|(^\s*$)",
                     line[:40], re.IGNORECASE)

    if match:
        is_comment = True
        executable_code = ""
    else:
        executable_code = line[:LINE_SIZE].rstrip()

        # regex to match and group labels, mnemonics and args
        complete_parse = re.match(
            r"(^\s*((?P<label>[a-z_][a-z0-9_]*):)?\s*(?P<extended>\+)?(?P<mnemonic>[a-z_]+)\s+(?P<args>.*)?)", line[:LINE_SIZE].upper(), re.IGNORECASE)

        if complete_parse:
            mnemonic = complete_parse.group("mnemonic")
            args = complete_parse.group("args")
            label = complete_parse.group("label")

            if complete_parse.group("extended") == "+":
                extended = True

    return Line(line, is_comment, executable_code, mnemonic, args, label, extended)


def pass_one(source_file: str):
    line_number, line_address, start_address, begin = 0, 0, 0, 0
    first_line, is_started = False, False
    program_name = None

    # reading file contents
    with open(source_file, "r") as file:

        while True:
            new_line = file.readline().expandtabs(8)
            if not new_line:
                sys.exit("Reached end of file without 'END' statement.")
                # or break ?

            line = get_line(new_line)

            # updating the user with current progress
            print(f"\rProcessing Line Number: {line_number}", end="")
            time.sleep(0.05)

            loc_ctr = 0

            if line.is_executable:
                # cecking and inserting label into SYMTAB
                if line.label and line.label in SYMTAB:
                    sys.exit(f"Lable is already defined: {line.label}.")
                elif line.label:
                    SYMTAB[line.label] = line_address

                # if start of code, setting first line_address(in HEX)
                if line.mnemonic == "START" and not is_started:
                    if Helpers.is_number(line.args) and int(line.args, 16) < MAX_SPACE:
                        line_address = int(line.args, 16)

                        SYMTAB = {x: line_address for x in SYMTAB}

                        program_name = line.label if line.label else ""
                        start_address = line_address
                        is_started = True
                    else:
                        sys.exit("Invalid Start Address.")

                elif line.mnemonic == "START" and is_started:
                    sys.exit("Multiple 'START' statements.")

                elif line.mnemonic == "END":
                    file_contents.append(line)
                    print("Pass One completed.")

                    return SYMTAB, file_contents

                elif line.mnemonic not in Opcodes.opcode.keys():
                    sys.exit(f"Invalid Mneomic {line.mnemonic}.")

                else:
                    loc_ctr = int(Opcodes.opcode[line.mnemonic]["Type"])
                    if not first_line:
                        begin = line_address
                        first_line = True

                if line.is_extended and Opcodes.opcode[line.mnemonic]["Type"] == 3:
                    loc_ctr = 4

                line_address = (line_address + loc_ctr) % MAX_SPACE

            # incrementing line number and appending file_contents
            line_number += 1
            file_contents.append(line)

    print("File parsing completed.")
    return SYMTAB, file_contents, program_name, start_address, begin

# here

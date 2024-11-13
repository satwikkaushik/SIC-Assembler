import csv
import sys

import models.Assembler_HW as Assembler_HW

PARENT_DIR = "temp_files"

global SYMTAB, LOCTR, START_LOC
SYMTAB: dict = {}
LOCTR = 0
START_LOC = 0

# line = {"loc": int, "label": str, "command": str, "args": list, "opcode": str}


def pass_() -> dict:
    out_file = open(f"{PARENT_DIR}/out_pass_one.csv", "w")
    in_file = open(f"{PARENT_DIR}/in_file.csv", "r")

    # making sure files are open
    if (out_file == None) or (in_file == None):
        sys.exit("Unable to read/write files.")

    # creating reader and writer objects
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)

    is_first_run: bool = True

    for row in reader:
        if is_first_run:
            if row[2] == "START":
                LOCTR = int(row[3], 16)
                START_LOC = LOCTR
                is_first_run = False
            else:
                sys.exit("START command not found.")
        else:
            row[0] = hex(LOCTR)[2:].upper()
            command_type = 0

            # checking for END statement
            if row[2] == "END":
                continue

            # adding lables into SYMTAB
            if row[1] != "None" and row[1] not in SYMTAB:
                SYMTAB[row[1]] = hex(LOCTR)[2:].upper()
            elif row[1] != "None" and row[1] in SYMTAB:
                sys.exit(f"Re-initialization of a variable: {row[1]}.")

            # checking correctness of OPCODE
            if row[2] not in Assembler_HW.opcodes:
                sys.exit(f"Invalid OPCODE: {row[2]}.")

            # updating LOCTR
            command_type = Assembler_HW.opcodes[row[2]]["Type"]
            if command_type == -1:
                if row[2] == "RESW":
                    command_type = 3 * int(row[3])
                elif row[2] == "RESB":
                    command_type = 1 * int(row[3], 10)
                elif row[2] == "BYTE":
                    if row[3][0] == 'C':
                        command_type = len(row[3]) - 3
                    elif row[3][0] == 'X':
                        command_type = 1
                elif row[2] == "WORD":
                    command_type = 3

            LOCTR += int(command_type)

        # writing row into out_file
        writer.writerow(row)

    in_file.close()
    out_file.close()

    return SYMTAB, hex(LOCTR - START_LOC)[2:].upper()

import csv
import sys

import models.Assembler_HW as Assembler_HW

# line = {"loc": int, "label": str, "command": str, "args": list, "opcode": str}

PARENT_DIR = "temp_files"


def extract(file):
    out_file = open(f"{PARENT_DIR}/in_file.csv", "w", newline="")
    in_file = open(file, "r")

    # making sure files are open
    if (out_file == None) or (in_file == None):
        sys.exit("Unable to read/write files.")

    # creating writer object for out_file
    writer = csv.writer(out_file)

    # operforming operations on each line
    for in_line in in_file:
        features: list = in_line.split(" ")
        out_line: list

        # skipping witing of comments and assembler directives
        if features[0] == "." or features[0] in Assembler_HW.directives:
            continue

        elif features[0] == "RSUB":
            features[1] = features[1][:-1]
            out_line = [-1, "None", features[0], "None", features[1], "None"]

        # line contains command and args only
        elif len(features) == 2:
            # removing new-line character
            features[1] = features[1][:-1]

            out_line = [-1, "None", features[0], features[1], "None"]

        # line contains lable, command and args
        else:
            # removing new-line character
            features[2] = features[2][:-1]

            out_line = [-1, features[0], features[1], features[2], "None"]

        # writing into file
        writer.writerow(out_line)

    in_file.close()
    out_file.close()

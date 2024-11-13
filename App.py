import os
import sys

import models.FeatureExtractor as FeatureExtractor
import models.PassOne as PassOne
import models.PassTwo as PassTwo
import models.ObjectCodeWriter as ObjectCodeWriter

"""
Main method
"""


def main():
    # inputting the source file
    source_file = input("Enter Source File(full path): ") or "test_file.txt"
    if not os.path.exists(source_file):
        sys.exit("File does not exist.")

    # inputting ouput file name
    out_file_name = input("Enter Object Code File Name: ") or "out.txt"
    out_file_name.replace(" ", "")

    # converting normal text file to a standard format for easy reading/writing
    FeatureExtractor.extract(source_file)

    # Pass One
    SYMTAB, PROG_SIZE = PassOne.pass_()

    # Pass Two
    PassTwo.pass_(SYMTAB)

    # finally writing the obejct file
    ObjectCodeWriter.write_code(PROG_SIZE, out_file_name)


if __name__ == "__main__":
    main()

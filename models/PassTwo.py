import sys
import csv
import models.Assembler_HW as Assembler_HW

PARENT_DIR = "temp_files"


def format_for_indexed_addressed(hex_str: str) -> str:
    bin_str = format(int(hex_str[0]), '04b')
    bin_str = '1' + bin_str[1:]
    return hex(int(bin_str, 2))[2:].upper() + hex_str[1:]


def for_other_cases(row) -> str:
    command = ""
    args = row[3]
    t_addr = ""
    is_index_addressed = False

    # determining opcode of command
    if row[2] in Assembler_HW.opcodes:
        command = str(Assembler_HW.opcodes[row[2]]["Code"])
    elif row[2] in SYMTAB:
        command = str(SYMTAB[row[2]])
    else:
        sys.exit(f"Undefined Symbol: {row[2]}")

    # determining TA

    if ",X" in args:
        is_index_addressed = True
        args = str(args).split(",")[0]

    # determing relative address
    if args in Assembler_HW.registers:
        t_addr = Assembler_HW.registers[args]
    elif args in SYMTAB:
        t_addr = SYMTAB[args]
    else:
        sys.exit(f"Undefined Label: {args} in line: {row}")

    # now modifying for indexed bit
    if is_index_addressed:
        t_addr = format_for_indexed_addressed(t_addr)

    obj_code = f"{command}{t_addr}"

    return obj_code


def for_byte(args) -> str:
    obj_code = ""
    if args.startswith("C’") and args.endswith("’"):
        ascii_values = [hex(ord(char))[2:].upper() for char in args[2:-1]]
        obj_code = "".join(ascii_values)
    elif args.startswith("X’") and args.endswith("’"):
        obj_code = args[2:-1]

    return obj_code


def pass_(SYMTAB_in):
    global SYMTAB
    SYMTAB = SYMTAB_in

    in_file = open(f"{PARENT_DIR}/out_pass_one.csv", "r")
    out_file = open(f"{PARENT_DIR}/out_pass_two.csv", "w")

    # ensuring files are open
    if (in_file is None) or (out_file is None):
        sys.exit("Unable to read/write files.")

    # creating reader and writer objects
    reader = csv.reader(in_file)
    writer = csv.writer(out_file)

    # [loc(0), label(1), command(2), args(3), obj_code(4)]

    # ---opcode-- x  -----TA-------
    # [bbbb-bbbb |b| bbb-bbbb-bbbb]
    # str: binary -> hex

    for row in reader:
        obj_code = ""

        # skipping for START
        if row[2] in Assembler_HW.has_no_opcode:
            obj_code = "None"

        # corner case of RSUB
        elif row[2] == "RSUB":
            obj_code = "4C0000"

        # corner case of BYTE
        elif row[2] == "BYTE":
            obj_code = for_byte(args=row[3])

        # corner case of WORD
        elif row[2] == "WORD":
            args = int(row[3], 16)
            obj_code = str(args)

            if len(obj_code) < 6:
                obj_code = ("0" * (6 - len(obj_code))) + obj_code

        # for other cases
        else:
            obj_code = for_other_cases(row)

        # writing object code in row
        row[-1] = obj_code
        # writing row in out_file
        writer.writerow(row)
    # end for
# end def

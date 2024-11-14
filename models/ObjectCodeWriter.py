import csv
import sys
import models.Assembler_HW as Assembler_HW

MAX_T_LEN = 60
PARENT_DIR = "temp_files"


def write_H_record(row: list, PROG_SIZE: str) -> tuple:
    result_str = f"H {row[1].ljust(6)} {row[3].zfill(6)} {
        PROG_SIZE.zfill(6)}\n"
    return (result_str, row[3])


def write_E_record(PROG_START_ADDR: str) -> str:
    return f"E {PROG_START_ADDR.zfill(6)}\n"


def write_T_record(start_addr: str, obj_codes: list) -> str:
    obj_code_str = "".join(obj_codes)
    length = len(obj_code_str) // 2
    return f"T {start_addr.zfill(6)} {format(length, '02X')} {obj_code_str}\n"


def write_code(PROG_SIZE: str, out_file_name: str) -> None:
    in_file = open(f"{PARENT_DIR}/out_pass_two.csv", "r")
    out_file = open(out_file_name, "w")

    # ensure both files are open
    if (in_file is None) or (out_file is None):
        sys.exit("Unable to read/write files.")

    # creating reader object
    reader = csv.reader(in_file)

    PROG_START_ADDR = None

    # object codes for text records
    current_text_start_addr = None
    current_text_obj_codes = []

    for row in reader:
        # write Header Record
        if row[2] == "START":
            result_str, PROG_START_ADDR = write_H_record(row, PROG_SIZE)
            out_file.write(result_str)

            current_text_start_addr = row[3]
            continue

        # skip
        if row[2] in Assembler_HW.has_no_opcode or row[4] == "None":
            if current_text_obj_codes:
                out_file.write(write_T_record(
                    current_text_start_addr, current_text_obj_codes))

                current_text_obj_codes = []
            current_text_start_addr = row[0]
            continue

        # accumulate object codes for the text record
        obj_code = row[4]
        if len("".join(current_text_obj_codes) + obj_code) > MAX_T_LEN:
            out_file.write(write_T_record(
                current_text_start_addr, current_text_obj_codes))

            current_text_start_addr = row[0]
            current_text_obj_codes = []

        current_text_obj_codes.append(obj_code)

    # write the last text record if any object code remains
    if current_text_obj_codes:
        out_file.write(write_T_record(
            current_text_start_addr, current_text_obj_codes))

    # write End Record
    result_str = write_E_record(PROG_START_ADDR)
    out_file.write(result_str)

    # closing files
    in_file.close()
    out_file.close()

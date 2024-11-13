"""
Just a container to organize things
"""

opcodes = {
    'ADD': {'Code': "18", 'Type': 3},
    'ADDF': {'Code': "58", 'Type': 3},
    'ADDR': {'Code': "90", 'Type': 2},
    'AND': {'Code': "40", 'Type': 3},
    'CLEAR': {'Code': "B4", 'Type': 2},
    'COMP': {'Code': "28", 'Type': 3},
    'COMPF': {'Code': "88", 'Type': 3},
    'COMPR': {'Code': "A0", 'Type': 2},
    'DIV': {'Code': "24", 'Type': 3},
    'DIVF': {'Code': "64", 'Type': 3},
    'DIVR': {'Code': "9C", 'Type': 2},
    'FIX': {'Code': "C4", 'Type': 1},
    'FLOAT': {'Code': "C0", 'Type': 1},
    'HIO': {'Code': "F4", 'Type': 1},
    'J': {'Code': "3C", 'Type': 3},
    'JEQ': {'Code': "30", 'Type': 3},
    'JGT': {'Code': "34", 'Type': 3},
    'JLT': {'Code': "38", 'Type': 3},
    'JSUB': {'Code': "48", 'Type': 3},
    'LDA': {'Code': "00", 'Type': 3},
    'LDB': {'Code': "68", 'Type': 3},
    'LDCH': {'Code': "50", 'Type': 3},
    'LDF': {'Code': "70", 'Type': 3},
    'LDL': {'Code': "08", 'Type': 3},
    'LDS': {'Code': "6C", 'Type': 3},
    'LDT': {'Code': "74", 'Type': 3},
    'LDX': {'Code': "04", 'Type': 3},
    'LPS': {'Code': "D0", 'Type': 3},
    'MUL': {'Code': "20", 'Type': 3},
    'MULF': {'Code': "60", 'Type': 3},
    'MULR': {'Code': "98", 'Type': 2},
    'NORM': {'Code': "C8", 'Type': 1},
    'OR': {'Code': "44", 'Type': 3},
    'RD': {'Code': "D8", 'Type': 3},
    'RMO': {'Code': "AC", 'Type': 2},
    'RSUB': {'Code': "4C", 'Type': 3},
    'SHIFTL': {'Code': "A4", 'Type': 2},
    'SHIFTR': {'Code': "A8", 'Type': 2},
    'SIO': {'Code': "F0", 'Type': 1},
    'SSK': {'Code': "EC", 'Type': 3},
    'STA': {'Code': "0C", 'Type': 3},
    'STB': {'Code': "78", 'Type': 3},
    'STCH': {'Code': "54", 'Type': 3},
    'STF': {'Code': "80", 'Type': 3},
    'STI': {'Code': "D4", 'Type': 3},
    'STL': {'Code': "14", 'Type': 3},
    'STS': {'Code': "7C", 'Type': 3},
    'STSW': {'Code': "E8", 'Type': 3},
    'STT': {'Code': "84", 'Type': 3},
    'STX': {'Code': "10", 'Type': 3},
    'SUB': {'Code': "1C", 'Type': 3},
    'SUBF': {'Code': "5C", 'Type': 3},
    'SUBR': {'Code': "94", 'Type': 2},
    'SVC': {'Code': "B0", 'Type': 2},
    'TD': {'Code': "E0", 'Type': 3},
    'TIO': {'Code': "F8", 'Type': 1},
    'TIX': {'Code': "2C", 'Type': 3},
    'TIXR': {'Code': "B8", 'Type': 2},
    'WD': {'Code': "DC", 'Type': 3},
    'BYTE': {'Code': "00", 'Type': -1},
    'WORD': {'Code': "00", 'Type': -1},
    'RESW': {'Code': "00", 'Type': -1},
    'RESB': {'Code': "00", 'Type': -1},
    'None': {'Code': "00", 'Type': 0}
}


registers = {'A': '0', 'X': '1', 'L': '2', 'PC': '8',
             'SW': '9', 'B': '3', 'S': '4', 'T': '5', 'F': '6'}

directives = ["BASE", "NOBASE"]

has_no_opcode = ["START", "END", "RESW", "RESB"]

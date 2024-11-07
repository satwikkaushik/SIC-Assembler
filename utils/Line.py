"""
Every line in the source file is converted to this object
Every feature of each line is extracted
"""


class Line:
    line: str = ""
    executable_code: str = ""
    mnemonic: str = ""
    args: str = ""
    label: str = ""
    is_extended: bool = False
    is_comment: bool = False

    def __init__(self, line, is_comment, executable_code, mnemonic, args, label, extended) -> None:
        self.line = line
        self.is_comment = is_comment
        self.executable_code = executable_code
        self.mnemonic = mnemonic
        self.args = args
        self.label = label
        self.extended = extended

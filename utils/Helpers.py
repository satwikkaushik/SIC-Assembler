"""
Contains methods that are useful though out the project
"""


# to check if a string can be converted to int
def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except:
        return False

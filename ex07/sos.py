import sys


def sos():
    """
This function takes a string as an argument and converts it into a Morse
code message. The function accepts only alphanumeric characters and the
conventional space (no other whitespace characters).

Parameters:
- sys.argv[1] (str): The string that will be encoded in Morse code.This
function takes a string as argument and turn it in a morse message, the
function accepts only alphanumeric characters and the space.

Returns:
- str: The Morse code representation of the input string.
"""
    MORSE = {" ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
                    "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                    "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                    "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
                    "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
                    "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "1": ".---- ",
                    "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
                    "6": "-..... ", "7": "--... ", "8": "---.. ",
                    "9": "----. ", "0": "----- "}
    try:
        if len(sys.argv) != 2 or not all(c.isalnum()
                                         or (c == ' ') for c in sys.argv[1]):
            raise AssertionError("AssertionError: the arguments are bad")
        else:
            string_to_encode = sys.argv[1].upper()
            encoded_string = ""
            for c in string_to_encode:
                encoded_string += MORSE[c]
            print(encoded_string)
    except AssertionError as Err:
        print(f"{Err}")


if __name__ == "__main__":
    sos()

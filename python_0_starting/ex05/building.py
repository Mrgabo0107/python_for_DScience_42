import sys
import string


def count(text):
    """
    This is the core of the program, here I'm doing all the counts

    Parameters:
    text (str): the string on which the sums will be performed
    """
    numb_of_chars = len(text)
    numb_of_upper = sum(1 for char in text if char.isupper())
    numb_of_lower = sum(1 for char in text if char.islower())
    numb_of_punctuation = sum(1 for char in text if char in string.punctuation)
    numb_of_spaces = sum(1 for char in text if char.isspace())
    numb_of_digits = sum(1 for char in text if char.isdigit())

    print(f"The text contains {numb_of_chars} characters")
    print(f"{numb_of_upper} upper letters")
    print(f"{numb_of_lower} lower letters")
    print(f"{numb_of_punctuation} punctuation marks")
    print(f"{numb_of_spaces} spaces")
    print(f"{numb_of_digits} digits")


def main():
    """
    This function counts and displays the sum of a upper-case, lower-case,
    punctuation characters, digits and spaces (taking the carriage return
    as a space) in a string passed as parameter.

    Parameters:
    argv[1]: the text to analyze (if no parameter is provided de program
    ask for)
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        count(text)
    except AssertionError as Err:
        print(f"Assertion error: {Err}")
    exit()


if __name__ == "__main__":
    main()

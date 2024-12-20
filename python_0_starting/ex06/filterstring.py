import sys


def main():
    """
This function does and returns a list with the substrings (separated
by space characters) of a string that have a length greater than a
given integer.

Parameters:
- sys.argv[1] (str): The string to split.
- sys.argv[2] (int): The comparison length.
"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        string = str(sys.argv[1])
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")
        separatedWords = string.split()
        list_to_return = [word for word in separatedWords
                          if (lambda word: len(word) > number)(word)]
        print(list_to_return)
    except AssertionError as Err:
        print(f"{Err}")


if __name__ == "__main__":
    # print(main.__doc__)
    main()

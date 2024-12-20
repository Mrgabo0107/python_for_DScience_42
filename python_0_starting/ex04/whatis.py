import sys


def main():
    try:
        if len(sys.argv) < 3:
            if len(sys.argv) == 2:
                try:
                    value = int(sys.argv[1])
                    if value % 2 == 0:
                        print("I'm Even")
                        return 0
                    else:
                        print("I'm Odd")
                        return 0
                except ValueError:
                    raise AssertionError("argument is not an integer")
            else:
                return 0
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as Err:
        print(f"AssertionError: {Err}")


if __name__ == "__main__":
    main()

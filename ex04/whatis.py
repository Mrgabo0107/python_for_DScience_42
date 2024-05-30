import sys

try:
    if len(sys.argv) < 3:
        if len(sys.argv) == 2:
            try:
                value = int(sys.argv[1])
                if value % 2 == 0:
                    print("I'm Even")
                    exit()
                else:
                    print ("I''m Odd")
                    exit()
            except ValueError:
                raise AssertionError("argument is not an integer")
        else:
            exit()
    else:
        raise AssertionError("more than one argument is provided")
except AssertionError as Err:
    print(f"AssertionError: {Err}")



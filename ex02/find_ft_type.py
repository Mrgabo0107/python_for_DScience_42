def all_thing_is_obj(object: any) -> int:
    # define the possible types
    types = {"list": "List",
             "tuple": "Tuple",
             "set": "Set",
             "dict": "Dict",
             "str": "Str"
             }

    # extract the type from the list:
    object_type = type(object)
    type_string = types.get(object_type.__name__, "Type not found")

    if type_string == "Str":
        print(f"{object} is in the kitchen : {object_type}")
    elif type_string != "Type not found":
        print(f"{type_string} : {object_type}")
    else:
        print(type_string)

    return 42

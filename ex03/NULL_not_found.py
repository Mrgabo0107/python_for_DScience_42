def NULL_not_found(object: any) -> int:
    types = {
        "NoneType" : "Nothing",
        "nan" : "Cheese",

    }
    object_type = type(object)

    

    print(object, object_type, object_type.__name__)
    return 1
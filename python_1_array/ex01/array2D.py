def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate a 2D array using slicing and return the new array.
    
    Args:
        family (list): A 2D array (list of lists).
        start (int): Starting index for slicing.
        end (int): Ending index for slicing.
    
    Returns:
        list: The truncated 2D array.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("All rows must have the same size")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    shape = (len(family), len(family[0]))
    print(f"My shape is: {shape}")
    truncated = family[start:end]
    new_shape = (len(truncated), len(truncated[0]) if truncated else 0)
    print(f"My new shape is: {new_shape}")
    
    return truncated
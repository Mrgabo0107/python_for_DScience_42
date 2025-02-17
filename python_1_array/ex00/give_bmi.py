def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Takes a list of heights and a list of weights with the same number of 
    elements and returns a list with the correspondent bmi. 
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("The height and weight parameters must be a list")
    if len(height) != len(weight):
        raise ValueError("The list must have the same length")
    if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All the elements in the lists must be int or float")
    if not all(h > 0 for h in height) or not all(w > 0 for w in weight):
        raise ValueError("All height and weight values must be positive")
    return [w / (h ** 2) for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compares a list of bmp's with a value and decide if the bmp is under this value
    """
    if not isinstance(bmi, list) or not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("The bmi parameter must be a list of int or float")
    if not isinstance(limit, int):
        raise ValueError("The limit must be an int")
    if not all(b > 0 for b in bmi):
        raise ValueError("All BMI values must be positive")
    if limit <= 0:
        raise ValueError("The limit must be a positive integer")
    return [b > limit for b in bmi]

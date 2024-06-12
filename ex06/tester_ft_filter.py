from ft_filter import ft_filter


print("Original .__doc__:\n")
print(filter.__doc__)
print("\nCopy .__doc__:\n")
print(ft_filter.__doc__)


def test_filter_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    originalResult = list(filter(lambda x: x % 2 == 0, numbers))
    myResult = list(ft_filter(lambda x: x % 2 == 0, numbers))
    assert originalResult == myResult, "problem!"
    print(f"\nTest1:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_words_starting_with():
    words = ["apple", "banana", "apricot", "cherry", "avocado"]
    originalResult = list(filter(lambda x: x.startswith('a'), words))
    myResult = list(ft_filter(lambda x: x.startswith('a'), words))
    assert originalResult == myResult, "problem!"
    print(f"\nTest2:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_non_empty_elements():
    items = ["text", "", None, "another text", 0, "0"]
    originalResult = list(filter(lambda x: x, items))
    myResult = list(ft_filter(lambda x: x, items))
    assert originalResult == myResult, "problem!"
    print(f"\nTest3:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_negative_numbers():
    numbers = [-1, 2, -3, 4, -5, 6]
    originalResult = list(filter(lambda x: x < 0, numbers))
    myResult = list(ft_filter(lambda x: x < 0, numbers))
    assert originalResult == myResult, "problem!"
    print(f"\nTest4:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_dictionary_by_value():
    dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    originalResult = dict(filter(lambda item: item[1] > 2, dictionary.items()))
    myResult = dict(ft_filter(lambda item: item[1] > 2, dictionary.items()))
    assert originalResult == myResult, "problem!"
    print(f"\nTest5:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_floats_greater_than():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    originalResult = list(filter(lambda x: x > 3.0, numbers))
    myResult = list(ft_filter(lambda x: x > 3.0, numbers))
    assert originalResult == myResult, "problem!"
    print(f"\nTest6:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_alphabetic_characters():
    string = "a1b2c3d4!#e*f"
    originalResult = ''.join(filter(str.isalpha, string))
    myResult = ''.join(ft_filter(str.isalpha, string))
    assert originalResult == myResult, "problem!"
    print(f"\nTest7:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_tuples_by_second_element_length():
    tuples = [(1, "a"), (2, "abc"), (3, "ab"), (4, "abcd")]
    originalResult = list(filter(lambda x: len(x[1]) > 2, tuples))
    myResult = list(ft_filter(lambda x: len(x[1]) > 2, tuples))
    assert originalResult == myResult, "problem!"
    print(f"\nTest8:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_lists_by_sum():
    list_of_lists = [[1, 2], [3, 4], [5, 6], [0, 0]]
    originalResult = list(filter(lambda x: sum(x) > 5, list_of_lists))
    myResult = list(ft_filter(lambda x: sum(x) > 5, list_of_lists))
    assert originalResult == myResult, "problem!"
    print(f"\nTest9:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_dicts_by_key_value():
    dicts = [{'name': 'Alice', 'age': 30},
             {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 25}]
    originalResult = list(filter(lambda x: x['age'] > 21, dicts))
    myResult = list(ft_filter(lambda x: x['age'] > 21, dicts))
    assert originalResult == myResult, "problem!"
    print(f"\nTest10:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_integers():
    numbers = [0, 1, 2, 0, 3, 0, 4]
    originalResult = list(filter(None, numbers))
    myResult = list(ft_filter(None, numbers))
    assert originalResult == myResult, "problem!"
    print(f"\nTest11:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_strings():
    strings = ["", "apple", "banana", "", "cherry"]
    originalResult = list(filter(None, strings))
    myResult = list(ft_filter(None, strings))
    assert originalResult == myResult, "problem!"
    print(f"\nTest12:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_mixed_list():
    mixed_list = [0, "apple", "", None, "banana", False, [], "cherry"]
    originalResult = list(filter(None, mixed_list))
    myResult = list(ft_filter(None, mixed_list))
    assert originalResult == myResult, "problem!"
    print(f"\nTest13:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_lists():
    list_of_lists = [[], [1, 2], [], [3], [], [4, 5, 6]]
    originalResult = list(filter(None, list_of_lists))
    myResult = list(ft_filter(None, list_of_lists))
    assert originalResult == myResult, "problem!"
    print(f"\nTest14:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_dicts():
    list_of_dicts = [{}, {'name': 'Alice'},
                     {}, {'name': 'Bob'}, {}, {'age': 30}]
    originalResult = list(filter(None, list_of_dicts))
    myResult = list(ft_filter(None, list_of_dicts))
    assert originalResult == myResult, "problem!"
    print(f"\nTest15:\nOriginal: {originalResult} \nMy Filter: {myResult}")


def test_filter_true_tuples():
    list_of_tuples = [(), (1, 2), (), (3,), (), (4, 5, 6)]
    originalResult = list(filter(None, list_of_tuples))
    myResult = list(ft_filter(None, list_of_tuples))
    assert originalResult == myResult, "problem!"
    print(f"\nTest16:\nOriginal: {originalResult} \nMy Filter: {myResult}")


if __name__ == "__main__":
    test_filter_even_numbers()
    test_filter_words_starting_with()
    test_filter_non_empty_elements()
    test_filter_negative_numbers()
    test_filter_dictionary_by_value()
    test_filter_floats_greater_than()
    test_filter_alphabetic_characters()
    test_filter_tuples_by_second_element_length()
    test_filter_lists_by_sum()
    test_filter_dicts_by_key_value()
    test_filter_true_integers()
    test_filter_true_strings()
    test_filter_true_mixed_list()
    test_filter_true_lists()
    test_filter_true_dicts()
    test_filter_true_tuples()

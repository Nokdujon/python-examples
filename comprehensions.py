"""Comprehensions in Python are a way to create a new sequence from an already existing sequence."""

# There are four main types of comprehensions in Python:
# - List comprehension
# - Dictionary comprehension
# - Set comprehension
# - Generator comprehension


def list_comprehension() -> None:
    """
    Function List comprehension
    The syntax for list comprehension is:
    [ <expression> for x in <sequence> if <condition>]
    """
    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # Ex1: List comprehension: updating the same list
    data = [x + 3 for x in data]
    print("Updating the list: ", data)

    # Ex2: List comprehension: creating a different list with updated values
    new_data = [x * 2 for x in data]
    print("Creating new list: ", new_data)

    # Ex3: With an if-condition: Multiples of four:
    fourx = [x for x in new_data if x % 4 == 0]
    print("Divisible by four", fourx)

    # Ex4: Alternatively, we can update the list with the if condition as well
    fourxsub = [x - 1 for x in new_data if x % 4 == 0]
    print("Divisible by four minus one: ", fourxsub)

    # Ex5: Using range function:
    nines = [x for x in range(1, 100) if x % 9 == 0]
    print("Nines: ", nines)


def dict_comprehension() -> None:
    """Function Dictionary comprehension
    The syntax for dictionary comprehension is:
    dict = { key:value for key, value in <sequence> if <condition> }
    """

    # Dictionary comprehension takes one or two lists as input and creates
    # a dictionary out of it. I will now demonstrate how this can be done using
    # only one list and by using two lists.

    # Using range() function and no input list
    using_range = {x: x * 2 for x in range(1, 13)}
    print("Using range(): ", using_range)

    # Lists
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "June",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Using one input list
    numbers_dict = {x: x**2 for x in numbers}
    print("Using one input list to create dict: ", numbers_dict)

    # Using two input lists
    months_dict = {key: value for (key, value) in zip(numbers, months)}
    print("Using two lists: ", months_dict)


def set_comprehension() -> None:
    """Set comprehension"""
    # The set comprehension deals with the set data type and it's very similar
    # to list comprehension. The only key difference is the use of curly
    # brackets for sets instead of square brackets as in lists.

    numbers_set = {x for x in range(10, 20) if x not in [12, 14, 16]}
    print(numbers_set)


def gen_comprehension() -> None:
    """Generator comprehension"""
    # Generator comprehensions are also very similar to lists with the
    # variation of using curved brackets instead of square brackets. They are
    # also more memory efficient as compared to list comprehensions.

    data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    gen_obj = (x for x in data)
    print(gen_obj)
    print(type(gen_obj))

    # The elements in this iterator object cannot be directly accessed and need
    # the help of a for loop and as such, I iterate over these elements and
    # print them.
    for items in gen_obj:
        print(items, end=" ")

"""Pure functions"""


def pure_function() -> None:
    """Pure function is a function that does not change or
    have any effect on a variable, data, list, or sets beyond its own scope."""

    numbers: list = [1, 2, 3]
    print("numbers =", numbers)  # [1, 2, 3]

    def add_to(item: int) -> list:
        """Function it changes the numbers by appending the item which
        is passed as an argument."""
        numbers.append(item)
        return numbers

    print("add_to(4) =", add_to(4))  # [1, 2, 3, 4]
    print("numbers =", numbers)  # [1, 2, 3, 4]

    def add_to_pure_function(lst: list, item: int) -> list:
        """Function a pure function, you need to think how to extend
        the function to accept a list as an argument, add the item to
        the list without modifying the original list, and how to return
        a new list with the newly added item.

        The solution is to create a new list and copy or clone the data from
        the original list."""

        new_numbers: list = lst.copy()
        new_numbers.append(item)
        return new_numbers

    print(
        "add_to_pure_function(numbers, 5) =", add_to_pure_function(numbers, 5)
    )  # [1, 2, 3, 4, 5]
    print("numbers =", numbers)  # 1, 2, 3, 4]

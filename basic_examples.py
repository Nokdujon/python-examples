"""essential examples"""


def loop() -> None:
    """_for-in statement_"""
    alphabets: str = "abcdefghijklmnopqrstuvwxyz"
    chars: list = ["a", "b", "c", "d", "e"]
    grades: dict = {
        "A": 90,
        "B": 80,
        "C": 70,
        "D": 60,
        "F": 59,
    }

    print("0. iterate in string")
    for char in alphabets:
        print(char, end=" ")
    print("", end="\n\n")

    print("1. iterate in list")
    for char in chars:
        print(char, end=" ")
    print("", end="\n\n")

    print("2. iterate in enumerate(list)")
    for idx, val in enumerate(chars):
        print(f"idx = {idx}, val = {val}", end=", ")
    print("", end="\n\n")

    print("3. iterate in dict.items() and print key and value")
    for key, val in grades.items():
        print(f'"{key}": {val}', end=", ")
    print("", end="\n\n")

    print("4. iterate in dict.items() and print item")
    for item in grades.items():
        print(f"item = {item}", end=", ")
    print("", end="\n\n")

    print("5. iterate in dict and print each pair")
    for grade in grades:
        print(f"grade = {grade}", end=", ")
    print("", end="\n\n")

    print('6. iterate in range(10) and print "hi"')
    for _ in range(10):
        print("hi", end=" ")
    print("", end="\n\n")

    print("7. iterate in range(10, -1, -1), count down!")
    for idx in range(10, -1, -1):
        print(idx, end=" ")
    print("", end="\n\n")


def use_print() -> None:
    """_examples of using the print function_"""

    favorite_player: str = "Dennis Bergkamp"
    favorite_number: int = 10
    favorite_football_club: str = "Arsenal FC"

    # print(*values: object, sep: str | None = " ", end: str | None = '\n')
    print("a", "b")  # a b
    print("c", "d", sep=", ")  # c, d
    print("e", "f", sep="; ", end=" ^^ ")  # e; f ^^
    print("g", "h")  # g h
    # a b
    # c, d
    # e; f ^^ g h

    print(
        "My favorite number is {1} because I like {0}.".format(
            favorite_player, favorite_number
        )
    )

    print(f"My favorite football club is {favorite_football_club}.")  # Support for 3.6+


total: int = 0


def use_global_variable() -> None:
    """_global-statement_
    Used when you use the "global" statement to update a global variable.
    Returns:
        _type_: _None_
    """

    global total

    def increase(number, interval):
        return number + interval

    for _ in range(10):
        total = increase(total, 1)
        print(f"total = {total},", end=" ")

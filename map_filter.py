"""map() and filter()"""

# the difference between a map and a filter function.
# A map takes all objects in the list and allows you to apply a function to it.
# A filter also allows you to take in all objects in the list and runs through
# a function but it creates a new list and only returns values where the
# evaluated function returns true.

menu: list[str] = ["americano", "orange juice", "mocha", "milk", "espresso", "beer"]
coffees: list[str] = ["americano", "mocha", "espresso", "latte"]


def find_coffee(beverage: str) -> bool:
    """Function find a coffee in the menu"""
    return True if beverage in coffees else False


mapped_result = map(find_coffee, menu)
filterred_result = filter(find_coffee, menu)

for item in mapped_result:
    print(f"mapped item = {item}")

for item in filterred_result:
    print(f"filterred item = {item}")

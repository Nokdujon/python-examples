mixed_fruits: str = "apple#banana#cherry#orange"
name: str = "heeseok"
text: str = "a fine day"

# str to list
fruits: list[str] = mixed_fruits.split("#", 3)
chars: list[str] = list(name)

# list to str
first_name: str = "".join(chars)
print(chars)
print(first_name)

# find in string
INTEGERS: str = "12345678901234512"
idx: int = INTEGERS.find("1", 11, -2)
reverse_idx: int = INTEGERS.rfind("1")
reverse_idx = INTEGERS.rfind("1", -7, -1)

# negative step parameter means that data is taken in reverse order
reversed_name: str = name[-1::-1]
reversed_name: str = name[::-1]

# str object is not an iterator
reversed_name: str = "".join(list(reversed(list(name))))

count_down: list[int] = [number for number in range(10, -1, -1)]

# String object is immutable.
# name[0] = 'H' wrong! using str.replace() instead of assignment.
new_name: str = name.replace("h", "H")

# count in string
print("abcc".count("c"))

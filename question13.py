lst = [1, 2, 3, "d", 4, 5, "a"]
numbers = [x for x in lst if isinstance(x, int)]
strings = [x for x in lst if isinstance(x, str)]
print("Numbers:", numbers)
print("Strings:", strings)
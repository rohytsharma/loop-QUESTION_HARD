string = "Hello 123"
digits = sum(c.isdigit() for c in string)
letters = sum(c.isalpha() for c in string)
spaces = sum(c.isspace() for c in string)
print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")
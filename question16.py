username = input("Enter username: ")
password = input("Enter password: ")
if (len(username) >= 5 )and len(password) >= 8:
    print("Valid")
else:
    print("Invalid")
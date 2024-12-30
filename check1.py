correct_username = "admin"
correct_password = "1234"

for attempts in range(3, 0, -1):
    print(f"Attempts left: {attempts}")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")
        if attempts > 1:
            continue
        else:
            print("You have been blocked.")
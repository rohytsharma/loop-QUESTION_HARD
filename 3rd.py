for i in range(3,0,-1):
    username_data = input("Enter your username: ")
    password_data = input("Enter your password: ")
    if username_data != "rohitsharma" or password_data != "Rohit@56":
        if i==1:
            print("you have been blocked")
            continue
        print(i-1,"attempt left")

    else:
        print("login successful")



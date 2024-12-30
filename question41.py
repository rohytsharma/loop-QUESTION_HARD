num = int(input("Enter a number: "))
if num == sum(int(d) ** len(str(num)) for d in str(num)):
    print("Armstrong")
else:
    print("Not Armstrong")
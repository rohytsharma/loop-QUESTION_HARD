num = int(input("Enter a number: "))
if num == sum(x for x in range(1, num) if num % x == 0):
    print("Perfect")
else:
    print("Not Perfect")
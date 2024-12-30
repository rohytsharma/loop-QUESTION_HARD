a=int(input("enter start: "))
b=int(input("enter end:"))
start=a
end=b
odd_sum = sum(x for x in range(start, end + 1) if x % 2 != 0)
print(odd_sum)
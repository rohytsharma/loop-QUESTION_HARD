odd_sum = sum(x for x in range(1, 101) if x % 2 != 0)
even_sum = sum(x for x in range(1, 101) if x % 2 == 0)
print(f"Odd sum: {odd_sum}, Even sum: {even_sum}")
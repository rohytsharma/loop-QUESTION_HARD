sample_list = str(input("Enter any list of numbers: "))
vowels = "aeiouAEIOU"
result = ''.join(c for c in sample_list if c not in vowels)
print(result)
sample_list = input("Enter any list of numbers: ")
sample_list_num = [int(x) for x in sample_list]
squares = [x ** 2 for x in sample_list_num]
print(squares)
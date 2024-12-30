sample_list = input("Enter any list of numbers: ")
sample_list_num = [int(x) for x in sample_list]
odd = [x for x in sample_list_num if x % 2 != 0]
even = [x for x in sample_list_num if x % 2 == 0]
print("Odd:", odd)
print("Even:", even)
'''
 Sum of a list
'''

sample_list = input("Enter any list of numbers: ")
sample_list_num = [int(x) for x in sample_list] #changing into tyo [1,2,3] walla from hai
print(sample_list_num)
b=0
for i in sample_list_num:
    b+=i
print(b)
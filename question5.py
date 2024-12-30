'''
multiplication of a each element. given list=[4,5,3,2]
'''
list=input("enter any list: ")
list_num=[int(x) for x in list]
print(list_num)
b= 1

for i in list_num:
    b = b*i
print(f"the total is: {b}")
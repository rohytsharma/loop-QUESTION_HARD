'''
write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
'''

my_list = [1, "a", "c", 2, 3, 4]
for item in my_list:
    if isinstance(item, int): #isinstance ley k garcha bhanda item ma bhako int matrai true huncha bhandincha
        print(item)
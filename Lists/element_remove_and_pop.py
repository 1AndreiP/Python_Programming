'''
Write a program to create a list and take user inputs to perform following operations: 
add element to the list 
remove elements from the list (using remove and pop ) 
'''

list=[]
for i in range(5):
    a=input("Add your element here: ")
    list.append(a)
print("This is the current list: ", list)
b=input("Remove a element from the list: ")
list.remove(b)
print("This is the current list: ", list)
c=int(input("Pop a element from the list: "))
list.pop(c)
print(list)
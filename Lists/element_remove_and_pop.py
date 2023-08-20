'''
Write a program to create a list and take user inputs to perform following operations: 
add element to the list 
remove elements from the list (using remove and pop ) 
'''

list=[]
while True:
    a=input("Add your element here: ")
    if a == "-1":
        break
    list.append(a)
print("This is the current list: ", list)
b=input("Remove a element from the list: ")
list.remove(b)
print("This is the current list: ", list)
c=int(input("Pop a element from the list: "))
list.pop(c)
print(list)
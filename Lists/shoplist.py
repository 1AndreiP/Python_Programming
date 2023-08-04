'''
Question: You are tasked with writing a Python program to manage a shopping list. 
The program should allow a user to add items to the list, remove items from the list, 
and display the current items on the list. Make sure your program can handle an empty shopping list. 

Sample Run: 
Add item to shopping list: apples 
Add item to shopping list: oranges 
Add item to shopping list: milk 
Current shopping list: ['apples', 'oranges', 'milk'] 
Remove item from shopping list: oranges 
Current shopping list: ['apples', 'milk'] 
'''

def shoplist(shop_list):
    for i in range(5):
        a=input("Add a item to the shopping list: ")
        shop_list.append(a)
        print("The item has been added to the shopping list.")
    print("Current shopping list: ", shop_list)
    b=input("Remove a item from shopping list: ")
    if b in shop_list:
        shop_list.remove(b)
        print("The item has been removed from the shopping list.")
    else:
        print("The item has not been in the shopping list. ")
    return("Current shopping list: ", shop_list)

print(shoplist([]))
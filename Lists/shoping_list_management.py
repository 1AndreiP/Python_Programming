'''
Welcome to the Shopping List Manager! 


Enter the items you want to add to your list (type 'done' to finish): 
Apples 
Milk 
Bread 
done 
Your Shopping List: 
1. Apples 
2. Milk 
3. Bread 
'''


list=[]
while True:
    a=input("Enter the items you want to add to your shopping list: ")
    if a.lower() == "done":
        break
    else:
        list.append(a)
print("Your Shopping List", list)
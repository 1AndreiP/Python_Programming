'''
Question 2: Extend and Remove 
Create a list called first_names with the elements: "Alice", "Bob", "Charlie". 
Create another list called last_names with the elements: "Johnson", "Smith", "Brown". 
Extend the first_names list using the elements from the last_names list. 
Remove "Smith" from the updated first_names list. 
Print the final version of the first_names list. 
'''

first_name=["Alice", "Bob", "Charlie"]
last_name=["Johnson", "Smith", "Brown"]
first_name.extend(last_name)
first_name.remove("Smith")
print(first_name)
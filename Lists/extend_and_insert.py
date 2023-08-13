'''
Question 5: Extend and Insert 

 

Create a list named colors with the elements: "red", "green", "blue". 

Create another list named additional_colors with the elements: "yellow", "orange". 

Extend the colors list with the elements from the additional_colors list. 

Insert "purple" at the beginning of the updated colors list. 

Print the final version of the colors list. 

 
'''

colors=["red", "green", "blue"]
additional_colors=["yellow", "orange"]
colors.extend(additional_colors)
colors.insert(0, "purple")
print(colors)
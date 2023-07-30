'''
Create a function that takes a list of values and returns the first and last values in a new list. 

Examples 

first_last([5, 10, 15, 20, 25]) ➞ [5, 25] 

first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True] 

first_last([None, 4, "6", "hello", None]) ➞ [None, None] 
'''

def first_last(lst):
    return(lst[0], lst[-1])

print(first_last([5,10,15,20,25]))
print(first_last(["edabit", 13, None, False, True]))
print(first_last([None, 4, "6", "hello", None]))
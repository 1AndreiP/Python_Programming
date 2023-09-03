'''
Create a function that takes a list and finds the integer which appears an odd number of times. 

Examples 

find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1 

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5 

find_odd([10]) ➞ 10 
'''

def find_odd(list):
    for i in range(len(list)):
        c=list.count(list[i])
        if c%2==1:
            return list[i]
print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))
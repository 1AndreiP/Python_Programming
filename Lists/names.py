'''
Question: Given a list of names, write a Python program that takes an input of a letter and
outputs the count of names that start with that letter. Ensure your program can handle a letter that doesn't start any names. 
Sample Run: 
Input Names: ['Adam', 'Brad', 'Charlie', 'Alice', 'Bruno', 'Clara'] 
Input Letter: 'A' 
Output: 2 
'''

def count_names(letter): 
    total = 0
    names=[]
    n = int(input("How many names you want: "))
    for i in range(n):
        a=input("Add the names: ")
        names.append(a)
    for i in range(len(names)):
        if names[i].startswith(letter):
            total=total + 1
    return total

print(count_names('A'))

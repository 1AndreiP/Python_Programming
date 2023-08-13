'''
Question 4: Append and Pop 

 

Create an empty list called stack. 

Append the integers 10, 20, and 30 to the stack list. 

Use the pop() method to remove and print the last element from the stack. 

Append 40 and 50 to the stack. 

Use the pop() method again to remove and print the last element from the stack. 

Print the final state of the stack. 
'''

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop(-1)
print(stack)
stack.append(40)
stack.append(50)
stack.pop(-1)
print(stack)
'''
Question: A teacher has a list of grades for students in a class, recorded as percentages. Write a Python program that accepts this
list of grades as input and outputs the highest grade, the lowest grade, and the average grade. Ensure your program can handle any number of grades in the list. 
Sample Run: 
Input: [85, 92, 78, 88, 76, 95, 89, 77, 84] 
Output: Highest grade: 95, Lowest grade: 76, Average grade: 85.1 
'''

def grades():
    n=int(input("Enter the number of students in class: "))
    grade=[]
    for i in range(n):
        a=int(input("Enter your grade: "))
        grade.append(a)
    total=sum(grade)
    average=total/n
    print("The Highest grade is", max(grade))
    print("The Lowest grade is", min(grade))
    print("The Average grade is", average)
print(grades())
'''
You are tasked with creating a program to keep track of your grades. Write a program that allows the user to 
input their grades for different subjects and then calculates the average grade. 
Sample Run 
Grades Tracker 
Enter the number of subjects: 4 
Enter the grades for each subject (separated by spaces): 
Math: 85 90 78 
English: 92 88 91 
Science: 75 82 88 
History: 89 78 85 
Average Grade: 84.25 
'''
'''
grades=[]
a=int(input("Enter the number of subjects: "))
for i in range(a):
    b=int(input("Enter the grade: "))
    grades.append(b)
total=sum(grades)
average=total/a
print(average)
'''
all_subject=[]
a=int(input("Enter the number of subjects: "))
for i in range(a):
    b=input("Enter the grades for each subject (separated by spaces): ")
    grade = b.split(" ")
    subject = grade[0]
    score = grade[1:]
    grades=[subject, score]
    print(grades)
    all_subject.append(grades)
    print(all_subject)
# (13.) Write a program to accept the marks of 6 students and display them in a sorted manner.

list = []
print("Marks of six student & displaying in sorted.")
num = int(input("Enter the number of student : "))
for i in range(0, num):
	marks = int(input())
	list.append(marks) 
print("Marks of ", num, "Students.")
print(list.sort())

#  (5.) Write a program to find the average of two numbers entered by the the users and also find the grade.

print("Marksheet of a student..")
print("Enter the marks of student in following subjects.")
comp  = input("Enter the marks obtained in computer  : ")
maths = input("Enter the marks ontained in maths     : ")
sci   = input("Enter the marks obtaine in science    : ")
sst   = input("Enter the marks obtained in sst       : ")
hindi = input("Enter the marks obtained in hindi     : ")
total = int(comp) + int(maths) + int(sci) + int(sst) + int(hindi); # total marks calculation.
percentage = (total / 500) *100; # calculating the percentage.
average = total / 5; #calulating average marks.

# code for printing the total marks, percentage gained, average marks. 
print("Total marks obtained      : ", total)
print("Average marks obtained    :", average)
print("Total percentage obtained : ", percentage, "%")

# Below code for checking the codtions for grade.
if (percentage >= 60):
    print ("Grade A.");
elif (percentage >= 45 and percentage < 60):
    print ("Grade B.");
elif (percentage >= 35 and percentage < 45):
    print ("Grade C");
else:
    print ("Fail");
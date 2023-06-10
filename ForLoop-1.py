# Example : 1
# Printing counting from using forloop by taking start & end position from user's.....
 
var1 = int(input("Enter the start range to print counting : "))
var2 = int(input("Enter the end range to print counting : "))
print("Printing counting from " + str(var1) + " to " + str(var2) + " : ")
for i in range (var1,var2):
    print(i)
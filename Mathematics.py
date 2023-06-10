#program for simple calculater in python
print("Python Program for Addition, Subtraction, Multiplication, Division")
print("") #it is for blank one line.
var1 = input ("Enter First Number : ") #inputting 1st number in var1 from user
var2 = input("Enter Second Number :") #inputting 2nd number in var2 from user
sum = int(var1) + int(var2) #for add
sub = int(var1) - int(var2) #for subtract
pro = int(var1) * int(var2) #for multiplucation
quo = int(var1) / int(var2) #for quotient
rem = int(var1) % int(var2) #for remainder
print("Sum of ",var1, "+", var2 , "=" , sum) #printing sum 
print("Difference of ",var1, "-", var2 , "=" , sub) #printing difference
print("Product of ",var1, "*", var2 , "=" , pro) #printing product 
print("Quotient of ",var1, "/", var2 , "=" , quo) #printing quotient
print("Remainder of ",var1, "%", var2 , "=" , rem) #printing remainder

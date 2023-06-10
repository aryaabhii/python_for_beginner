# Example : 8
# Factorial

fact =1 
var = int(input("Enter Number : "))
while var >= 1:
    fact = fact * var
    var -= 1
print("Factorial of ",var, ":", fact)
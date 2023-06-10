# Example : 5
# Printing odd & even number by getting inputs from users.
print("Example of odd and even number : ")
var1 = int(input("Enter from where you want start : "))
var2 = int(input("Enter from where you want end   : "))
while var1 <= var2:
    if var1 % 2 == 0:
        print("Even number : ", var1)
    else:
        print("Odd number  : ", var1)
    var1 += 1

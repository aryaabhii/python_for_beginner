# Python Function with Arguments With Return Value

def Adding(f,s):
    # print ("Sum of", f, "+", s, " = " , f + s)
    return (f + s)
var1 = int(input("Enter first number  : "))
var2 = int(input("Enter second number : "))
Adding(var1, var2)
print("Sum :", Adding())
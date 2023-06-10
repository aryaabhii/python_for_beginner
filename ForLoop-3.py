# Example : 3
# Prf for odd & even number using for loop..

print ("Enter the start & end range to check odd & even number :")
var1 = int(input("Enter the range for start : "))
var2 = int(input("Enter the range for stop : "))
for i in range(var1,var2):
    if i % 2 == 0:
        print("Even : ",i)
    else:
        print("Odd  : ",i)
    

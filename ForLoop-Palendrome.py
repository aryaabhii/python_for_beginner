# Example : 6
#  Q. What is Palindrome Number ?
# ->  

var1 = int(input("Enter a number : "))
var2 = var1
rev = 0
#for i in range (var1,0,-1):
while(var1 > 0):
    rev = rev * 10 + var1 % 10
    var1 = var1 // 10
if var2 == rev:
    print(var2,"is palindrome")
else:
    print(var2,"is not palindrome")
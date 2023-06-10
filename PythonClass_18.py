# (18.) Greatest number among 4 inputted number.

var1 = int(input("Enter first number  : "))
var2 = int(input("Enter second number : "))
var3 = int(input("Enter third number  : "))
var4 = int(input("Enter fouth number  : "))

if(var1 > var2):
    if(var1 > var3):
        if(var1 > var4):
            print(var1, "Is greatest number.")
        else:
            print(var4, "Is greatest number.")
    elif(var2 > var3):
        print(var2, "Is greatest number.")
    else:
        print(var3, "Is greatest number.")
elif(var3 > var4):
    print(var3, "Is greatest number.")
else:
    print(var4, "Is greatest number.")




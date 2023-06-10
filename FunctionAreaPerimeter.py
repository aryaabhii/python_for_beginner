# Example : 2
# Program to calculate the area & perimeter of a rectangle......
# Area function..
def Area(l, w):
    print("Area      of Rectangle having length [",l,"] & width [", w,"] = ", l * w)

# Perimeter function..
def Peri(l, w):
    print("Perimeter of Rectangle having length [",l,"] & width [", w,"] = ", 2 * (l + w))

# Code for inputting the value.
var1 = int(input("Enter length of rectangle : "))
var2 = int(input("Enter width of rectangle  : "))
Area(var1, var2) # calling area function .....
Peri(var1, var2) # calling peri  function .....
#Type conversion in python
# here we use type conversion to convert variable (bith_year) into an integer.
# int is a builtin function.
birth_year = input("Enter your birth year: ")
age = 2022 - int(birth_year)
print("Your age : ", age)

# float is also a built in function
# we use float for decimal value
float()

# bool is also a built in function
# we use bool for true or false
bool()

# str is also a built in function
# we use str for string
bool()

# write a program for basic calculator for integer
first = input("Enter first number = ")
second = input("Enter second number = ")
sum = int(first) + int(second)
print("Sum of first & second number = " + str(sum)) # here variable sum is type casted into string, so we got the answer bcz pyhon only concat srings.

# write a program for basic calculator for float
first = input("Enter first number = ")
second = input("Enter second number = ")
sum = float(first) + float(second)
print("Sum of first & second number = ", sum)

# Another ways to solve above questions.
# for example:
# write a program for basic calculator for float
first = float(input("Enter first number = "))
second = float(input("Enter second number = "))
sum = first + second
print("Sum of first & second number = " +  str(sum))

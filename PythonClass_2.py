# (2.) Write a python program to find the remainder when a number is divided by z(integer).
print("Python program to find the remainder & quotient.")
dividend = int(input("Enter Dividend : "))
divisor = int(input("Enter Divisor : "))
quotient, remainder = divmod(dividend, divisor)
print("Quotient of ", dividend, "%", divisor, "=", quotient)
print("Raminder of ", dividend, "%", divisor, "=", remainder)

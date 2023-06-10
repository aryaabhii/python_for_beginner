# range functions in python

# range function used for genrating sequence of numbers. 
print("------- Printing the number from 0 to 4 index ---------") 
numbers = range(5)  
for number in numbers:
    print(number)

print("------- Printing the number from 6 to 10 index ---------") 
numbers = range(6, 10)  # 6 is the staring point and 10 is the ending. 
for number in numbers:
    print(number)

print("------- Printing the number from 6 to 10 by increasing 2 ---------") 
numbers = range(6, 10, 2)  # 6 is the staring point, 10 is the ending & 2 is the escaping sequence. 
for number in numbers:
    print(number)

# we can also use range function inside the for loop
print("------- Printing the number from 0 to 4 using range inside the for loop ---------") 
for number in range(5):
    print(number)
     
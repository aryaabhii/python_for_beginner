# (12.) Write a program to store seven fruits in a list entered by the user.

# an empty list
list = []

print("N Number of Fruits entry in list : ")
# number of elements as input
num = int(input("Enter number of fruits : "))

# iterating till the range
for i in range(0, num):     # here 0 is the starting index & num is the last ending where loop will be end  
	fruits = str(input())
	list.append(fruits) # adding fruits name in list
print((list))


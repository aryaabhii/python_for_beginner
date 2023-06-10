# list methods or array in python

# if we want to insert 6 in the below list then we have to use 'append' function to insert 6 at the end.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# if we want to insert -1 in the below list then we have to use 'insert' function to insert -1 at the mid or begining.
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1) # here 0 is the index number & -1 is the value which have to put on 0 index.
print(numbers)

# if we want to remove -1 in the below list then we have to use 'remove' function to remove.
numbers = [-1, 1, 2, 3, 4, 5]
numbers.remove(-1)  # here, we have to pass the which have to remove from the list.
print(numbers)

# if we want to remove all items from the list we have to use 'clear' function.
numbers = [-1, 1, 2, 3, 4, 5]
numbers.clear() # here is no needed to pass anythings. 
print(numbers)

# if we want to check value is in list ot not have to use 'in' keywords.
numbers = [1, 2, 3, 4, 5]
print(5 in numbers) # result will be true bcz 5 us availabe in this list.
print(10 in numbers) # result will be false bcz 10 us noy availabe in this list.

# if we want to count the total of value in list we have to use 'len' function.
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # result will be 5 bcz 5 numbers in this list.
# lists or array in python

# we use list to represent list of objects
# Example:1
names = ["Sonu","Abhijeet","Akshay","Monu"]
print (names)

# Example:2
# if we pass index number then it will print only the value of that index
names = ["Sonu","Abhijeet","Akshay","Monu"]
print (names [3]) # so here, i'm passing 3rd index number then it will print 3rd object of right side i.e. Monu.

# Example:3
# if we pass index number then it will print only the value of that index
names = ["Sonu","Abhijeet","Akshay","Monu"]
print (names [-4]) # so here, i'm passing 3rd index number then it will print -4th object of left side i.e. Sonu.

# Example:4
# we can also change the object of an index
names = ["Sonu","Abhijeet","Akshay","Monu"]
names[0] = "Anurag"
print (names [-4]) # so here, i'm passing 3rd index number then it will print -4th object of left side i.e. Sonu.

# Example:5
# we can also print a specfic index like 1 to 3,
names = ["Sonu","Abhijeet","Akshay","Monu"]
print (names [0:2]) # so here, i'm passing starting and ending of list so the result will be ["Sonu","Abhijeet"]
print (names) # it will print our original list without any changes.
# Strings in python
tutorial = 'Learning Python.' # here tutorial storing a string object

# if we try to print only tutorial only we will got the defalult value, i.e. Learning Python. 
print (tutorial.upper()) # upper function will captalise each strings.
print (tutorial.lower()) # lower function will print each strings in small letter.
print (tutorial.find('P')) # find function help to find the letter index number.(her i'm passing the L as argument so the L is at start & the index number is staring from 0 so i got result = 0)
print (tutorial.find('Python')) # also we can pass word as argument to find index.
print (tutorial.replace('Python', '0')) # replace function is used for replacing the characters.
print ('Python' in tutorial) # in is a special type of keyword in python also known as operator.here if python will in string will got true result or if not then false. (here it is the example of boolean).


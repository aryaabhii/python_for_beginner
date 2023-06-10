# Operator precedence in python

var = 10 + 3 * 2 # if we print this we got result 16 bcz here multiplication (*) has higher precedence
print('Result = ' + str(var))

var = (10 + 3) * 3 # but in this case we got result 39 bcz here parantesis has higher precidence
print('Result = ' + str(var))

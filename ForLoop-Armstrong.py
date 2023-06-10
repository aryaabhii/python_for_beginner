# Example : 5
# Prg for armstrong number.......
#  Q. What is Armstrong Number ?
#  -> The sum of cube is equal to inputted number i.e. called armstong number.
#  -> for ex: 153 is arm strong number bcz (1*1*1 + 5*5*5 + 3*3*3) = 153.
# Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number: "))
sum = 0 #initilizing of sum...
temp = num # here passing original number in temp variable..
for i in range (temp, 0, -1):
   rem = temp % 10 # dividing inputed num e.g. 153 % 10 : 3 util its index no 0.
   sum = sum + (rem *  rem * rem)
   temp = temp // 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
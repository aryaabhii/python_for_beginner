# if statement in python

# we use if statement for decision making

temp = 25

if temp > 30:
    print ("It's hot day.")
    print ("Drink cold water.")
elif temp > 20:  # [20, 30]
    print ("It's a nice day.")
elif temp > 10: #[10,20]
    print ("It's little bit cold.")
else:
    print ("It's cold day.")

 
# Exercise: wight converter
weight = int(input ("Enter your weight : "))
unit = input("(K)g or (L)bs: ")
if unit.upper == "K":
    converted = weight / 0.45
    print ("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print ("weight in Kgs: " + str(converted))

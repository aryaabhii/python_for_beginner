# (17.) Program to calculate the bill of a customer.

print("\n")
print(" -------- Customer Personal Details -------- ")
Cid = int(input("Enter id               : "))
Cname = input("Enter name             : ")
phone = int(input("Enter phone number    : "))
address =  input("Enter address        : ")
print("\n")
print(" -------- Bill Information -------- ")
pasubit = int(input("Enter past unit     : "))
conunit = int(input("Enter consumed unit : "))
mrent = int(20); # fixed meter rent amount for all.
unit =  pasubit - conunit
if(unit < 100):
    total = unit * 3.5
    discount = (total * 3.25)/100
    tpay = total - discount + mrent
elif(unit > 100 and unit <= 200):
    total = unit * 3.5
    discount = (total * 4.5)/100
    tpay = total - discount + mrent
elif(unit > 200 and unit <= 300):
    total = unit * 3.5
    discount = (total * 5.25)/100
    tpay = total - discount + mrent
else:
    total = unit * 3.5
    discount = (total * 7.25)/100
    tpay = total - discount + mrent

print("--------------------------------------")
print("Total unit consumed  : ", float(unit))
print("--------------------------------------")
print("Meter rent           : ", mrent)
print("--------------------------------------")
print("Total bill           : ", float(total))
print("--------------------------------------")
print("Diccounted amount    : ", float(discount))
print("--------------------------------------")
print("Gross payable amount : ", float(tpay))
print("--------------------------------------")
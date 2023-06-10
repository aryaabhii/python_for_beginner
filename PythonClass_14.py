# (15.) Check that a tuple cannot be changed in Python. 

name = ["Anurag", "Abhijeet", "Akshay"]
nam2 = list(name);
nam2[2] = "Abhishek"
name = tuple(nam2)
nam2[1] = "Akshay" #can't chnage bcz tuple is define just before.
print(name) 


class Mgm:
    def __init__(etc, name, age, sal, deg):
        etc.name = name
        etc.age = age
        etc.sal = sal
        etc.deg = deg
    def myfun(self):
        print(self.name, self.age, self.sal, self.deg)
obj = Mgm("Abhijeet",20, 2000, "Developer")
obj.myfun()

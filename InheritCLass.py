# inheritance example......
class Mgm:
    def __init__(etc, name, age, sal, deg):
        etc.name = name
        etc.age = age
        etc.sal = sal
        etc.deg = deg
    def myfun(etc):
        print(etc.name, etc.age, etc.sal, etc.deg)
class Detail(Mgm):
    def __init_ (etc, name, age, sal, deg):
        etc.name = name 
        etc.age = age
        etc.sal = sal
        etc.deg = deg
    
obj = Detail("Sumesh",20, 2000, "SEO Expert")
obj.myfun()

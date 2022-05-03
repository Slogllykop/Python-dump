class Programmer:
    compnay = "MCOE"
    def __init__(self, name, salary, product):
        self.name = name
        self.salary = salary
        self.product = product
    def getInfo(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The Salary of the programmer is {self.salary}")
        print(f"The Product of the programmer is {self.product}")
        
Indraneel = Programmer("Indraneel", 100000, "GFX")
Sameer  = Programmer("Sameer", 100000, "Gnadu")
Yash = Programmer("Yash", 100000, "Bozo")   
Indraneel.getInfo()
Sameer.getInfo()
Yash.getInfo()
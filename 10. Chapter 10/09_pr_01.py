class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(
            f"The name of the programmer is {self.name} and the product is {self.product}")


vipul = Programmer("Vipul", "skype")
alka = Programmer("Alka", "Github")
vipul.getinfo()
alka.getinfo()
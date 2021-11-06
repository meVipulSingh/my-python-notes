class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} is square of {self.number**2}")

    def cube(self):
         print(f"The value of {self.number} is cube of {self.number**3}")


    def squareroot(self):
         print(f"The value of {self.number} is squareroot of {self.number**0.5}")


a = calculator(9)
a.square()
a.squareroot()
a.cube()
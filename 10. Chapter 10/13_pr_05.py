class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats avilable on train is {self.seats}")

    def fareInfo(self):
        print(f"The fare of the Train is Rs. {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry this train is full! Kindley try in tatkal")
    def cancelTicket(self):
        self.seats = self.seats+1

rajdhani = Train("rajdhani Express: 14015", 90, 300)
rajdhani.getStatus()
rajdhani.bookTicket()
rajdhani.getStatus()
rajdhani.cancelTicket()
rajdhani.getStatus()
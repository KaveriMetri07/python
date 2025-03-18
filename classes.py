class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passanger=[]

    def add_passenger(self,name):
        if not self.open_seat():
            return False
        self.passanger.append(name)
        return True
    def open_seat(self):
        return self.capacity-len(self.passanger)
    

flight=Flight(3)
peoples=["harry","harmeione","aiden","kaveri"]
for person in peoples:
    if flight.add_passenger(person):
        print(f"{person} is added to the flight")
    else:
        print(f"{person} no Available seats")
    

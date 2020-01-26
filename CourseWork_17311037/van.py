from vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, vehName, numDoors, numWheels, fuelConsumation, numRearDoors, numSideDoors):
        super().__init__(vehName, numDoors, numWheels, fuelConsumation)
        self.rearDoors = numRearDoors
        self.sideDoors = numSideDoors
        self.type = 'Van'

    # Overwriting function
    def printSpecs(self):
        print(self.name, self.doors, self.wheels, self.make, "Rear doors -", self.rearDoors, "Side doors -", self.sideDoors)
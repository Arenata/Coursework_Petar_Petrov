from vehicle import Vehicle

class Lorry(Vehicle):
    def __init__(self, vehName, numDoors, numWheels, fuelConsumation, trailer, maxLoad):
        super(Lorry, self).__init__(vehName, numDoors, numWheels, fuelConsumation)
        self.trailer = trailer
        self.load = maxLoad
        self.type = 'Lorry'

    # Overwriting function
    def printSpecs(self):
        print(self.name, self.doors, self.wheels, self.make, "Trailer -", self.trailer, "Max load -", self.load)
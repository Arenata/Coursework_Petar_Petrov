class Vehicle:

    def __init__(self, vehName, numDoors, numWheels, fuelConsumation):
        self.name = vehName
        self.doors = numDoors
        self.wheels = numWheels
        self.make = 'Generic Engines'
        self.type = 'Vehicle'
        self.fuelConsumation = fuelConsumation

    def printSpecs(self):
        print (self.name, self.doors, self.wheels, self.make)

    def printType(self):
        print ('Vehicle type: ' + self.type)

    def printDistanceConsumation(self, kilometers):
        liters = kilometers / 100 * self.fuelConsumation

        print(str(liters) + ' liters of fuel for ' + str(kilometers) + ' kilometers')



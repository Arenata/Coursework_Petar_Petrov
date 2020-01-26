from van import Van
from lorry import Lorry

def main():

    iceCreamVan = Van("Ice Cream Van", 2, 4, 10, 2, 1)
    bigGreenLorry = Lorry("My Big Green Lorry", 2, 8, 13, True, 75)

    iceCreamVan.printSpecs()
    iceCreamVan.printType()
    iceCreamVan.printDistanceConsumation(1000)

    bigGreenLorry.printSpecs()
    bigGreenLorry.printType()
    bigGreenLorry.printDistanceConsumation(555)

main()

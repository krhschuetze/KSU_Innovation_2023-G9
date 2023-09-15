# All types of container inherit from ContainerSpace
class ContainerSpace():
    # Interior dimensions in inches
    def __init__(self):
        self.type = "NULL"
        self.length = 999999999
        self.width = 999999999
        self.height = 999999999
        self.maxWeight = 999999999

# Shipping Containers (10, 20, 40)
class ShippingContainer(ContainerSpace):
    type = "NULL"
    # Each child of ShippingContainer has a different length
    width = 96
    height = 102
    maxWeight = 59200

class ShippingContainer10(ShippingContainer):
    type = "10 foot Shipping Container"
    length = 120
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer
    # Inherit maxWeight from ShippingContainer

class ShippingContainer20(ShippingContainer):
    type = "20 foot Shipping Container"
    length = 240
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer
    # Inherit maxWeight from ShippingContainer

class ShippingContainer40(ShippingContainer):
    type = "40 foot Shipping Container"
    length = 480
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer
    # Inherit maxWeight from ShippingContainer

# Box Truck
class BoxTruck(ContainerSpace):
    type = "Box Truck"
    length = 288
    width = 96
    height = 96
    maxWeight = 999999999

# Storage Unit
class StorageUnit(ContainerSpace):
    type = "Storage Unit"
    length = 576
    width = 480
    height = 96
    maxWeight = 999999999

# Available/Remaining space
class RemainingSpace(ContainerSpace):
    # Set all self variables to value of container type (Passed in)
    def __init__(self, containerType):
        self.type = "Remaining space in a " + containerType.type
        self.length = containerType.length
        self.width = containerType.width
        self.height = containerType.height
        self.maxWeight = containerType.maxWeight
    # Print dimensions
    def printDimensions(self): 
        print(self.type,
            "\nLength:", self.length,
            "\nWidth:", self.width,
            "\nHeight:", self.height)
    # Space filling method
    def howManyFit(self, item):
        counterLength = 0
        while (item.length <= self.length and item.width <= self.width and item.height <= self.height and item.weight <=self.maxWeight):
            self.length -= item.length
            self.width -= item.width
            self.height -= item.height
            self.maxWeight -= item.weight
            counterLength += 1
        counterWidth = 0
        while (item.length <= self.length and item.width <= self.width and item.height <= self.height and item.weight <=self.maxWeight):
            self.length -= item.length
            self.width -= item.width
            self.height -= item.height
            self.maxWeight -= item.weight
            counterWidth += 1
        counterHeight = 0
        while (item.length <= self.length and item.width <= self.width and item.height <= self.height and item.weight <=self.maxWeight):
            self.length -= item.length
            self.width -= item.width
            self.height -= item.height
            self.maxWeight -= item.weight
            counterHeight += 1
        counterWeight = 0
        while (item.length <= self.length and item.width <= self.width and item.height <= self.height and item.weight <=self.maxWeight):
            self.length -= item.length
            self.width -= item.width
            self.height -= item.height
            self.maxWeight -= item.weight
            counterHeight += 1
        return max(counterLength, counterWidth, counterHeight, counterWeight)

#EXAMPLE OBJECT
class itemExample:
    def __init__(self):
        self.type = "Car Battery"
        self.length = 2
        self.width = 5.5
        self.height = 8 + (15/16)
        self.weight = 7
    def printDimensions(self): 
        print(self.type,
            "\nLength:", self.length,
            "\nWidth:", self.width,
            "\nHeight:", self.height)





#Print dimensions testing 
boxTru = RemainingSpace(BoxTruck)
print(boxTru.printDimensions())
shipCon10 = RemainingSpace(ShippingContainer10)
print(shipCon10.printDimensions())
shipCon20 = RemainingSpace(ShippingContainer20)
print(shipCon20.printDimensions())
shipCon40 = RemainingSpace(ShippingContainer40)
print(shipCon40.printDimensions())

print("-----------------------------------------")

#Maximum amount of inputs testing
print("RemainingSpaceInUnit\n")
storUnit = RemainingSpace(ShippingContainer10)
print(storUnit.printDimensions())
print("\nObject Dimensions\n")
battery = itemExample()
battery.printDimensions()
print("\nHow many DID fit?\n")
print(storUnit.howManyFit(battery))
print("\nRemaining after subraction\n")
print(storUnit.printDimensions())
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

# Pallets
class Pallet(ContainerSpace):
    type = "Pallet"
    length = 48
    width = 60
    height = 40
    maxWeight = 4600

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
            "\nLength:", self.length, "inches",
            "\nWidth:", self.width, "inches",
            "\nHeight:", self.height, "inches",
            "\nWeight limit has not been reached.", self.maxWeight, "pounds remaining for use.")
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

#Generic object to ship
class ItemToShip:
    # Define all hazard labels an item can have
    hazardSet = {"acidic", "caustic", "combustible communicable", 
             "compressed gas", "corrosive", "explosive", 
             "explosive", "flammable", "infectious", 
             "inflammable", "poison", "radioactive",
             "refrigerated", "toxic", "volatile"}
    # Assign individual object variables- Potentially set this to many presaved
    def __init__(self, type, length, width, height, weight, hazards):
        self.type = type
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.hazards = hazards # Input hazards as a set- This disallows duplicates
    def printDimensions(self): 
        print(self.type,
            "\nLength:", self.length, "inches",
            "\nWidth:", self.width, "inches",
            "\nHeight:", self.height, "inches",
            "\nWeight:", self.weight, "pounds",
            #"\nHazards:", self.hazards
            )
        for hazard in self.hazardSet:
            if (hazard in self.hazards): print("Item is " + hazard.title())



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
print("Original space in Shipping Container with a length of 10 ft")
ship10 = RemainingSpace(ShippingContainer10)
print(ship10.printDimensions())
print("\nObject Dimensions\n")
battery = ItemToShip("Car Battery", 9.56, 6.875, 8.875, 34, {"flammable", "radioactive"})
battery.printDimensions()
print("\nHow many of " + battery.type + " fit in " + ship10.type + "?\n")
batteriesFit = ship10.howManyFit(battery)
print(batteriesFit)
print("\nSpace remaining after", batteriesFit, battery.type, "have been placed intside", ship10.type, "\n")
print(ship10.printDimensions())
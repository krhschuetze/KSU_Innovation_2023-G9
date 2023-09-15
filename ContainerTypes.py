# All types of container inherit from ContainerSpace
class ContainerSpace():
    # Interior dimensions in inches
    def __init__(self):
        self.type = "NULL"
        self.length = -999
        self.width = -999
        self.height = -999

# Shipping Containers (10, 20, 40)
class ShippingContainer(ContainerSpace):
    type = "NULL"
    # Each child of ShippingContainer has a different length
    width = 96
    height = 102

class ShippingContainer10(ShippingContainer):
    type = "10 foot Shipping Container"
    length = 120
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

class ShippingContainer20(ShippingContainer):
    type = "20 foot Shipping Container"
    length = 240
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

class ShippingContainer40(ShippingContainer):
    type = "40 foot Shipping Container"
    length = 480
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

# Box Truck
class BoxTruck(ContainerSpace):
    type = "Box Truck"
    length = 288
    width = 96
    height = 96

# Storage Unit
class StorageUnit(ContainerSpace):
    type = "Storage Unit"
    length = 576
    width = 480
    height = 96

# Available/Remaining space
class RemainingSpace(ContainerSpace):
    # Set all self variables to value of container type (Passed in)
    def __init__(self, containerType):
        self.type = "Remaining space in a " + containerType.type
        self.length = containerType.length
        self.width = containerType.width
        self.height = containerType.height
    # Print dimensions
    def printDimensions(self): 
        print(self.type,
            "\nLength:", self.length,
            "\nWidth:", self.width,
            "\nHeight:", self.height)
    # Space filling method
    


boxTru = RemainingSpace(BoxTruck)
print(boxTru.printDimensions())

shipCon10 = RemainingSpace(ShippingContainer10)
print(shipCon10.printDimensions())

shipCon20 = RemainingSpace(ShippingContainer20)
print(shipCon20.printDimensions())

shipCon40 = RemainingSpace(ShippingContainer40)
print(shipCon40.printDimensions())

storUnit = RemainingSpace(StorageUnit)
print(storUnit.printDimensions())
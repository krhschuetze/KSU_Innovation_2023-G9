# All types of container inherit from ContainerSpace
class ContainerSpace():
    # Interior dimensions in inches
    length
    width
    height

# Shipping Containers (10, 20, 40)
class ShippingContainer(ContainerSpace):
    # Each child of ShippingContainer has a different length
    width = 96
    height = 102

class ShippingContainer10(ShippingContainer):
    length = 120
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

class ShippingContainer20(ShippingContainer):
    length = 240
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

class ShippingContainer40(ShippingContainer):
    length = 480
    # Inherit width from ShippingContainer
    # Inherit height from ShippingContainer

# Box Truck
class BoxTruck(ContainerSpace):
    length = 288
    width = 96
    height = 96

# Storage Unit
class StorageUnit(ContainerSpace):
    length = 576
    width = 480
    height = 96
"""
test of reliable car class
"""

from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Crappy car", 100, 40)
print(unreliable_car)
unreliable_car.drive(50)
print(unreliable_car)
"""
Unreliable Car Class
child of parent class (Car)
"""
from car import Car
from random import uniform

class UnreliableCar(Car):
    """ Car class with a reliability object """

    def __init__(self, name, fuel, reliability: float):
        """ Initialise Car object, pulling from Car class parent, and adding reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        """Chance of how reliable car is."""
        if uniform(0, 100) < self.reliability:  # roll dice on reliability using uniform random
            while distance > self.fuel:  # while reliable distance travelled related to fuel left
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        else:
            distance = 0
        return distance
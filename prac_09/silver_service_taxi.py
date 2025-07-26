"""
Silver Service Taxi Class
child of taxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ A child of the taxi class, therefore inherits from taxi and car classes """
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """ passing in Car class objects, adding fanciness object """
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness  # fanciness is a scaler of all taxi's price per km

    def get_fare(self):
        """Override get_fare from Taxi Class to add a premium flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string of objects from all classes"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
"""
testing Silver Service Taxi Class.
"""


from silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Black & White", 100, fanciness=1.5)
silver_service_taxi.start_fare()
silver_service_taxi.drive(31)
print(silver_service_taxi)
print(f"Premium Fare: ${silver_service_taxi.get_fare():.2f} includes flagfall of: ${silver_service_taxi.flagfall:.2f}")

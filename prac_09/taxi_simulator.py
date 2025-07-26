"""
Taxi Simulator Practical
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    """Main program to simulate taxi service."""
    current_taxi = None
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill_to_date = 0

    print("Let's drive!")
    while True:
        print(MENU)
        print(f"Bill to date: ${bill_to_date:.2f}")
        choice = input(">>> ").strip().lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option.")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("\nTaxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    print("\nThank you for using the Taxi Simulator!")

def drive_taxi(current_taxi, bill_to_date):
    """Handle driving and fare calculation."""
    while True:
        try:
            distance = int(input("Drive how far? "))
            if distance < 0:
                print("Distance must be non-negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    current_taxi.start_fare()
    current_taxi.drive(distance)
    current_fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
    return bill_to_date + current_fare

def choose_taxi(taxis):
    """Allow the user to select a taxi from the list."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    while True:
        try:
            taxi_index = int(input("Choose taxi: "))
            if 0 <= taxi_index < len(taxis):
                if taxis[taxi_index].fuel <= 0:
                    print(f"{taxis[taxi_index].name} has no fuel. Choose a different taxi.")
                else:
                    return taxis[taxi_index]
            else:
                print(f"Invalid choice. Please choose a number between 0 and {len(taxis) - 1}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
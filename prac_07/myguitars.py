import csv
from guitar import Guitar


def main():
    """Main function to manage guitar collection."""
    print("My Guitar Collection!")
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    if not guitars:
        print("No guitars found. Let's add some!")
    else:
        print("\nLoaded guitars:")
        display_guitars(guitars)

        print("\nSorted by year (oldest to newest):")
        guitars.sort()
        display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars(filename, guitars)
    print(f"\n{len(guitars)} guitars saved to {filename}")


def load_guitars(filename):
    """Load guitars from CSV file."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:  # Ensure valid data format
                    try:
                        name = row[0].strip()
                        year = int(row[1])
                        cost = float(row[2])
                        guitars.append(Guitar(name, year, cost))
                    except ValueError:
                        print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty list.")
    return guitars


def display_guitars(guitars):
    """Display guitars with vintage status."""
    for i, guitar in enumerate(guitars, 1):
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_status}")


def add_new_guitars(guitars):
    """Add new guitars from user input."""
    print("\nAdd new guitars (leave name blank to stop)")
    while True:
        name = input("Name: ").strip()
        if not name:
            break

        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            if year < 0 or cost < 0:
                print("Year and cost must be positive numbers")
                continue

            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input - please enter valid numbers")


def save_guitars(filename, guitars):
    """Save guitars to CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in sorted(guitars):  # Save sorted by year
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
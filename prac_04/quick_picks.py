import random

# CONSTANTS
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

# Ask the user how many quick picks they want
quick_picks_count = int(input("How many quick picks? "))

for _ in range(quick_picks_count):
    quick_pick = []

    # Generate unique numbers for the quick pick
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    # Sort the numbers in ascending order
    quick_pick.sort()

    # Print each number, formatted to 2 spaces
    print(" ".join(f"{number:2}" for number in quick_pick))

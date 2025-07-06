"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


import random

# Main function
def main():
    # Get user input for the score
    score = float(input("Enter your score (0-100): "))
    # Determine and print the result based on the user-provided score
    result = determine_result(score)
    print(f"Your result is: {result}")

    # Generate a random score and determine the result
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(random_score)
    print(random_result)

# Function to determine the result based on score
def determine_result(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 50:
            print("Passable")
        if score > 90:
            print("Excellent")
    if score < 50:
        print("Bad")

# Run the program
if __name__ == "__main__":
    main()



# score_menu.py

MENU_OPTIONS = {
    'G': 'Get a valid score',
    'P': 'Print result',
    'S': 'Show stars',
    'Q': 'Quit'
}


def main():
    score = get_valid_score()
    choice = get_menu_choice()

    while choice != 'Q':
        handle_menu_choice(choice, score)
        if choice == 'G':
            score = get_valid_score()
        choice = get_menu_choice()

    print("Goodbye! Thanks for using the score menu.")


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive."""
    score = input_int("Enter score (0-100): ")
    while not (0 <= score <= 100):
        print("Invalid score. Must be between 0 and 100.")
        score = input_int("Enter score (0-100): ")
    return score


def input_int(prompt):
    """Safely get an integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; please enter a number.")


def get_menu_choice():
    """Display the menu and return a validated uppercase choice."""
    print("\nMenu:")
    for key, description in MENU_OPTIONS.items():
        print(f"({key}) {description}")
    choice = input(">>> ").strip().upper()
    while choice not in MENU_OPTIONS:
        print("Invalid choice. Please try again.")
        choice = input(">>> ").strip().upper()
    return choice


def handle_menu_choice(choice, score):
    """Dispatch function based on menu choice."""
    actions = {
        'P': lambda s: print(f"Result: {determine_result(s)}"),
        'S': lambda s: print_stars(s),
        'G': lambda s: None  # score handled in main for reassignment
    }
    action = actions.get(choice)
    if action:
        action(score)


def determine_result(score):
    """Return a string result based on score."""
    score_ranges = {
        range(90, 101): "Excellent",
        range(75, 90): "Good",
        range(50, 75): "Pass",
        range(0, 50): "Fail"
    }
    return next((label for rng, label in score_ranges.items() if score in rng), "Invalid")


def print_stars(score):
    """Print stars equal to the score."""
    print("*" * score)


if __name__ == "__main__":
    main()

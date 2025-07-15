def get_password(min_length):
    password = input(f"Enter a password (minimum {min_length} characters): ")
    while len(password) < min_length:
        print(f"Error: Password must be at least {min_length} characters long.")
        password = input(f"Enter a password (minimum {min_length} characters): ")
    return password


def print_asterisks(password):
    print('*' * len(password))


def main():
    MIN_LENGTH = 8
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


if __name__ == "__main__":
    main()

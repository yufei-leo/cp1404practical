# Part 1:
def get_numbers():

    numbers = []
    for i in range(5):
        number = int(input(f"Number {i + 1}: "))  # Get user input and convert it to an integer
        numbers.append(number)  # Add the number to the list
    return numbers

def display_number_info(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

numbers = get_numbers()
display_number_info(numbers)

# Part 2:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")

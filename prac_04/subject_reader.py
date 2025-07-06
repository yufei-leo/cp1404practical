"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()

    for subject in data:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []

    for line in input_file:
        line = line.strip()  # Remove the newline character
        parts = line.split(',')  # Split the line into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subjects.append(parts)  # Add the list of parts to the subjects list

    input_file.close()
    return subjects  # Return the nested list of subjects

main()

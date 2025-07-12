"""
Estimate:  3 hours
Actual:   around 5-6 hours
"""

import csv
from datetime import datetime
from operator import attrgetter
from project import Project


def main():
    """Main function for project management system."""
    print("Welcome to Pythonic Project Management")
    default_filename = "projects.txt"

    projects = load_projects(default_filename)
    print(f"Loaded {len(projects)} projects from {default_filename}")

    while True:
        display_menu()
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if confirm_save(default_filename):
                save_projects(default_filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                try:
                    project = Project(*row)
                    projects.append(project)
                except (ValueError, IndexError):
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost_estimate,
                project.completion_percentage
            ])
    print(f"{len(projects)} projects saved to {filename}")


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("\nIncomplete projects: ")
    for project in sorted(incomplete, key=attrgetter('priority')):
        print(f"  {project}")

    print("\nCompleted projects: ")
    for project in sorted(complete, key=attrgetter('priority')):
        print(f"  {project}")


def filter_projects_by_date(projects):
    try:
        date_string = input("Show projects that start after date (dd/mm/yy): ")
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

        filtered = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered, key=attrgetter('start_date')):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")

    try:
        project = Project(name, start_date, priority, cost_estimate, completion)
        projects.append(project)
        print(f"{project} added.")
    except ValueError:
        print("Invalid input - project not added")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        project.update(
            int(new_completion) if new_completion else None,
            int(new_priority) if new_priority else None
        )
        print("Project updated")
    except (ValueError, IndexError):
        print("Invalid selection")


def confirm_save(filename):
    response = input(f"Would you like to save to {filename}? ").lower()
    return response.startswith('y') or 'yes' in response


def display_menu():
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


if __name__ == "__main__":
    main()
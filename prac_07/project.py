from datetime import datetime


class Project:
    """Represent a Project object."""

    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if project is complete (100%), False otherwise."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Less than, used for sorting Projects by priority."""
        return self.priority < other.priority

    def update(self, completion_percentage=None, priority=None):
        """Update project completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority
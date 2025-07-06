class ProgrammingLanguage:
    def __init__(self, name, typing, reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        return f"{self.name},  {self.typing}, Reflection = {self.reflection}, First appeared in {self.year}"

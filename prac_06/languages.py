from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print(ruby)
print(visual_basic)
print("The dynamically typed languages are:")
for language in [python, ruby, visual_basic]:
    if language.is_dynamic():
        print(language.name)

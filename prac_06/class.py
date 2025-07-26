# monsters = [["Mike", 340, "blue"],
#             ["James", 14, "green"],
#             ["Randall", 24, "purple"]]
#
# scary_monsters = [monster for monster in monsters if monster[1] > 16]
#
# print(scary_monsters)

#
# class Monster:
#     def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#
#     def is_scary(self):
#         return self.number_of_teeth > 16 or self.colour == "red"
#
#
# monsters = [
#     Monster("Mike", 340, "blue"),
#     Monster("James", 14, "green"),
#     Monster("Randall", 24, "purple")
# ]
#
# scary_monsters = [monster for monster in monsters if monster.is_scary()]

class User:
    def __init__(self, name):
        self.name = name
        self.tacos = 5
        self.score = 0

    def give_tacos(self, other_user):
        if self.tacos > 0:
            self.tacos -= 1
            other_user.tacos += 1

    def __str__(self):
        return f"{self.name}, {self.score} points,{self.tacos} tacos left"

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokomen Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type",["electric", "Water", "Fire"])
#
# # table.align = "l"
#
# print(table)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print( "Woof!" )
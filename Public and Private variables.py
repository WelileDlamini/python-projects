# private
# abstraction
class PlayerCharacter:
    def __init__(self,name, age): # self represents playercharacter
        self._name = name
        self._age = age

    def run(self):
        return self

    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')
player1 = PlayerCharacter('welile',50)
print(player1.speak())# absstarction is taking place here, no need to know how speak was implemented
print(player1.speak)

# underscore means dont touch this (denotes privacy), should not be modified
# the __init__ is a dunder method(built in python)

# inheritance
class User: # parent class
    def sign_in(self):
        print('logged in')

class Wizard(User): #subclass inheritance, children classes, derived classses
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User): #subclass inheritance
    def __init__(self,name,num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows
    def attack(self):
        print(f'attacking with arrows of {self.num_of_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Mevin', 100)
print(wizard1.sign_in())
print(wizard1.attack())
print(archer1.attack())

# checking for instances
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1,User))
print(isinstance(wizard1, object))#automatic object that comes with python


# polymorphism
class User: # parent class
    def sign_in(self):
        print('logged in')

class Wizard(User): #subclass inheritance, children classes, derived classses
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User): #subclass inheritance
    def __init__(self,name,num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows
    def attack(self):
        print(f'attacking with arrows of {self.num_of_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Mevin', 100)

def player_attack(char): # this is called polymorphism
    char.attack()
player_attack(wizard1)
player_attack(archer1)

for char in [wizard1,archer1]:
    char.attack()









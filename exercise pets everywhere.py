class Pets:
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance


# super()
class User: # parent class
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User): #subclass inheritance, children classes, derived classses
    def __init__(self,name,power,email):
        User.__init(self,email)

        # or
        super().__init__(email) # when using super you dont pass self

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
wizard1 = Wizard('Welile', 50, 'welile@gmail.com')
print(wizard1.email)
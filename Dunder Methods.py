class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age

action_figure = Toy('red', 50)
print(action_figure.__str__()) # double underscore they are dunder methods
print(str(action_figure))

# exercise, extending list
class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))

# multiple inheritence
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

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self,name,power,arrows):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)
hb1 = HybridBorg('borgi', 50)
print(hb1.attack())


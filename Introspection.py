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
print(dir(wizard1))
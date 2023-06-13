class BigObject: # class or blueprint
    # code
    pass
obj1 = BigObject() # instanciate
print(type(obj1))

# Object oriented programming
class PlayerCharacter:
    # Class Object Attribute, its not dynamic its static
    membership = True
    def __init__(self,name, age):
        if PlayerCharacter.membership:
            self.name = name # attributes
            self.age = age

    def shout(self):# run is an attribute
     print(f'my name is {self.name}')

    def run(self,hello):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Welile',44) # objects
player2 = PlayerCharacter('Ndabenhle',50) # objects
player2.attack = 50

print(player1.age)
print(player2.age)
print(player2.attack)
print(player2.membership)
print(player1.membership)
print(player1.shout())
print(player2.shout())
print(player1.run('hello'))

# init
class PlayerCharacter:
    # Class Object Attribute, its not dynamic its static
    membership = True
    def __init__(self,name='welile', age=0):
        if age>18:
            self.name = name # attributes
            self.age = age

    def shout(self):  # run is an attribute
        print( f'my name is {self.name}' )
player1 = PlayerCharacter('Tom', 10)

print(player1.shout())


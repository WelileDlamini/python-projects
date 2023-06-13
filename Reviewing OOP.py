class NameOfClass: # class that needs to get instatiated
    class_attribute = 'value' # class object attributes
    def __init__(self,param1, param2):
        self.param1= param1 # attributes for instatiotion
        self.param2= param2

    def method(self): # methods, how to add them to our class
            #code

    # methods that can be called to the class without instatioting the obhect
    @classmethod
    def cls_method(cls,param1,param2):
        #code

    @staticmethod
    def cls_method2(param1,param2):
        # code

# developer fundamentals
class PlayerCharacter:
    def __init__(self,name, age): # self represents playercharacter
        self.name = name
        self.age = age

    def run(self):
        return self
player1 = PlayerCharacter('welile',50)
print(player1.run())


# encapsulataion
class PlayerCharacter:
    def __init__(self,name, age): # self represents playercharacter
        self.name = name
        self.age = age

    def run(self):
        return self

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')
player1 = PlayerCharacter('welile',50)
print(player1.speak())

# abstraction
class PlayerCharacter:
    def __init__(self,name, age): # self represents playercharacter
        self.name = name
        self.age = age

    def run(self):
        return self

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')
player1 = PlayerCharacter('welile',50)
print(player1.speak())# absstarction is taking place here, no need to know how speak was implemented



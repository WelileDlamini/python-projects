class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def wag_tail(self):
        print("Tail wags happily.")

my_dog = Dog("Buddy", "Golden Retriever")
print("My dog's name is", my_dog.name)
print("My dog's breed is", my_dog.breed)

my_dog.bark()
my_dog.wag_tail()
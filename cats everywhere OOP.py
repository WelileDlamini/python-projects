cats = []
class Cat:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        cats.append(self)
cat1 = Cat("Bubbles", 4)
cat2 = Cat("Theo", 5)
cat3 = Cat("Granny", 7)

def find_oldest(list):
    return max([k.age for k in cats])
print(f"The oldest cat is {find_oldest(cats)} years old.")



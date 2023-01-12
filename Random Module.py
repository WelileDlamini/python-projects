import random
random_integer = random.randint(1, 10)
print(random_integer )
random_flot = random.random() * 5
print(random_flot)


# lists
states_of_america = ["Delaware", "Pennsylvania", "Texas", "New York"]
print(states_of_america[3])
states_of_america[0] = "Pencilvana"
print(states_of_america )
states_of_america.append("Angelaland")
print(states_of_america )
#
states_of_america.extend(["Angelaland", "Jackbuyer","Swaziland"])
print(states_of_america )

# coding exercise
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to buy the meal")

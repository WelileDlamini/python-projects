enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")
# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()

# Global scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion()

# the is no block scope
game_level = 3
enemies = ["skeleton", "Zombie", "Allien"]
if game_level < 5:
    new_enemy = enemies[0]

# modifying a global scope
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# modifying a global scope
enemies = 1
def increase_enemies():
    print( f"enemies inside function: {enemies}" )
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# global constants
PI = 3.14159
def calc():
    PI =



class Car:
    vroom = 200

    def _init_(self, name, color, top_speed, status):
        self.brand = name
        self.color = color
        self.speed = top_speed
        self.available = status
        print("you just made a ", self.brand)

    def spray_paint(self, new_color):  # is a function or car class
        current_color = self.color  # lone variable
        self.color = new_color

        print("we've changed the color from " + current_color + " to " + self.color, ", nice choice")  # add the string that tells us what object has changed

    def engine_upgrade(self):
        self.speed += 10

    def car_availability(self):
        print(self.available)

    def compare_objects(self, vroom):
        if vroom == self.speed:
            print('Equal')
        elif vroom < self.speed:
            print('Greater')
        else: print('Lesser')

# use this to build a function than increases the speed of a caa object by 10 for every call
# create a function that prints out the status of the car object
#create a function that compares the objects speed to the 'vrrom' and prints a comparison for greater than less than and equal to

ferrari = Car('ferrari', "blue", 260, True)  # ferrari is an object of the car class

ferrari.spraypaint("red")

new_name = input("what is the name of the car :\n")
new_speed = input("what is the speed of the car :\n")
int(new_speed)
new_color = input("what is the color of the car :\n")
news_status = input("what is the status of the car :\n").title()
bool(new_status)
buggati = Car(new_color, new_status,)

# session lasted 2 hours and we disscused inheritance

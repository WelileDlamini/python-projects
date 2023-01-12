fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale","Tomatoes", "Celery" ,"Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][3])
fruits[-1] = "sugar"
fruits.append("lemons")
print(fruits)

# coding exercise
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0]) #2
vertical = int(position[1]) #3
selected_row = (map[vertical - 1])
selected_row[horizontal - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


import turtle
wn = turtle.Screen()
sukram = turtle.Turtle()

right_side = sukram.window_width()/2  # get window width and divide it by two
top_side = sukram.window_height()/2  # get window height and divide it by two

sukram.goto(right_side, top_side)     # have turtle draw line from center (0,0) to top-right corner

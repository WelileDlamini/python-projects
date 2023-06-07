def say_hello():
    print('hellooo')

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
fill = "*"
empty = ' '
def show_tree():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print( empty, end='' )
            elif pixel == 1:
                print( fill, end='' )
        print( ' ' )
show_tree()
show_tree()

# parameters vs arguments
def sy_hello(name,surname):
    print(f'hello {name}, {surname}')

#arguments
say_hello('Andrei', 'Dlamini')# calling , invoking the function

# keyword arguments
sy_hello(surname='dalmini', name= 'welile')
# default parameters
def sy_hello(name='Darth Vader',surname= 'dlamini'):
    print(f'hello {name}, {surname}')

# return
def sum(num1,num2):
    return num1 + num2


sum(4,5)
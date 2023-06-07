picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

#  iterate
# if 0 print ''
# if 1 print *
fill = "*"
empty = ' '
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(empty , end='')
        elif pixel == 1:
            print(fill ,end='')
    print(' ') # need a new line after every row
# developer fundamentals
# clean
# readibility

# find duplicates
# execise check for duplicates
some_list = ['a','b','c','b','d','m','n','n']
duplicate = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)
   
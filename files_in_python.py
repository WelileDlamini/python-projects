my_file = open('test.text')

print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.close()
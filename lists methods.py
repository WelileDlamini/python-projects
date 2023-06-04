basket = [1,2,3,4,5]
#adding
basket.append(100)
basket.insert(4,100)
new_list = basket
print(new_list)
print(basket)
# removing
basket.pop()
basket.pop(0)
basket.remove(4)
basket.clear()
print(basket)
# index
basket_1 = ['a','b','c','d','e','z','j','y']
print(basket_1.index('d',0,4))
# or
print('x' in basket_1)
print('i' in 'hi my name is welile dlamini')
# count
print(basket_1.count('d'))

# sort
basket_1 = ['a','b','c','d','e','z','j','y']
basket_1.sort()
print(basket_1)
# reverse
basket.sort()
basket.reverse()
print(basket)


# join
basket_1 = ['a','b','c','d','e','z','j','y']
basket.sort()
basket.reverse()
sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','JOJO'])
print(new_sentence)


# list unpacking
a,b,c = [1,2,3]
print(a)
print(b)
print(c)
a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
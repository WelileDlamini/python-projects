# fixing the errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# print is your friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)

# using a Debugger
def mutate(a_list):
    b_list =[]
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
    mutate([1,2,3,5,8,13])

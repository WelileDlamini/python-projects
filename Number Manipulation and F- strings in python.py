# print(round(8 / 3, 2))
# print(8 // 3)
result = 4 / 2
result /= 2
print(result)
#
#
# score = 0
# # user scores a point
# score += 1
# print(score)
#
# score = 0
# height = 1.8
# is_swimming = True
# # f-String
# print(f"your score is {score}, your height is{height}, you are winning is {is_swimming}")
# # interactive coding exercise

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
years_remaining = 90 - age_int
days = 365 * years_remaining
weeks = 52 * years_remaining
months = 12 * years_remaining
massage = f"you have {days} days, {weeks} weeks, and {months} months."
print(massage)




# dictionaries
customer = {
    "name": "Jone Smith"
    "age" "30",
    "is_verified": True
}
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
print(customer["name"])
print(customer.get("name"))

# challange
phone = input("phone: ")
digit_mapping = {
    "1": "one",
    "2": "Two",
    "3": "three",
    "4": "four"
}
output = ""
for character in phone:
    output += digit_mapping.get(character, "!" ) + " "
print(output)

# emoji convertor

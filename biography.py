# In Biology, the animal kingdom is separated into nine taxonomic ranks. Below is a very rough sketch
# of classification tree for animals. Write a program called ‘biology.py’ to determine the type of an
# animal based on the following simple classification scheme
print("Welcome to the Biolody expert")
type_of_skeleton = input("What is the skeleton type?:'internal' or 'external'")
if type_of_skeleton == "internal":
    fertilization = input("is fertilization 'within the body' or 'outside the body'")
    if fertilization == 'within the body':
        production = input("How are young produced? 'waterproof eggs' or 'live birth'")
        if production == "waterproof eggs":
            skin_cover = input("what is the cover of the skin? 'scales' or 'feathers'")
            if skin_cover == "scales":
                print("reptiles")
            elif skin_cover == "feathers":
                print("Bird")
        else:
            print("Mammal")
    location = input("Where does it live? 'in water' or 'near water'")
    if location == "in water":
        print("Fish")
    else:
        print("Amphibian")
else:
    print("Arthropod")





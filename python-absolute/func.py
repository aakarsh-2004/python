def hemlo_world(name):
    return 'Hemlo ' + name + '!'

greeting = hemlo_world('Aakarsh')

print(greeting)

# String methods!!

user_name = "Aakarsh Beohar!!"
print(user_name.replace("Aakarsh", "Anshu"))
print(user_name.find("A"))
print(user_name.split(" "))
print(user_name.capitalize())
print(user_name.center(50, "."))
print(user_name.count("a"))
print(user_name.endswith("!!"))
print(user_name.startswith("A"))
print(user_name.find("h"))
print(user_name.index("h"))
# Characters and numbers included
print(user_name.isalnum())
# Only characters included
print(user_name.isalpha())

print(user_name.swapcase())


if "ingapinga" == "ingapinga":
    print(True)
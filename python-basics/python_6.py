# dictionary methods

user = {
    "name": "Aakarsh",
    "age": 18,
    "gender": "male"
}

print(list(user.keys()))
print(list(user.values()))


print(list(user.items()))
# user.clear()
print(user.pop('age'))

# .popitem() method mostly removes the last element but sometimes it also randomly pops out any key-value pair
print(user.popitem())

# updating the value if it's present, if it is not then it gets created
user.update({"age": 45})

print(user)
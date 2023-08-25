# dictionaries are same as objects

user = {
    "name": "Aakarsh",
    "gender": "male",
    "age": 18,
    "hobbies": ["gaming", "coding", "travelling"],
    "education": "BTech'27"
}
# avoids error which we get if we use directly square brackets
print(user.get("status", "single"))


# creating dictionary with the function

user_two = dict(name = "Abhay", gender = "Male", age = 18)

print(user_two)

print(("name" in user_two) and ("name" in user))


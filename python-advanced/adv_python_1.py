# == is a comparison operator and it automatically alter the datatype for conversion if it needs to
# "is" keyword on the other hand checks if both the variables are stored in a same memory location

a = 1
b = 1
print(a is b) # will return True

# Damn I am liking python so far, never expected that

# "in" and "not in" are the only membership operators
for i in range(1):
    print("Hemlo world")

# the i variable we initialized with the loop above is permanent unlike other languages, in the end it stores the last value of the data it can access
print(i)

user = {
    "name": "Aakarsh",
    "age": 18,
    "is_cool": True
}
for k,v in user.items():
    print(k, v)
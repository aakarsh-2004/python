# List comprehension
my_list = [char for char in "hey"]
print(my_list) # returns ['h', 'e', 'y']

new_arr = [num for num in range(0, 10)]
# list comprehension with condition
new_arr = [num for num in range(0, 10) if num % 2 == 0]
print(new_arr)



# Dictionary comprehension
simple_dict = {"a": 1, "b": 2, "c": 4}
my_dict = {k:v**2 for k,v in simple_dict.items()}
print(my_dict)


# set comprehension
new_dict = {n for n in "aabbcc"}
print(new_dict)
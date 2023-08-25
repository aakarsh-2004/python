my_tuple = (1, 2, 3, 4)

print(type(my_tuple))

for item in my_tuple:
    print(item, end=" ")

print()
# my_tuple[0] = 1 # Action not possible
print(my_tuple)

if (2) in my_tuple:
    print("Yess!!")
else:
    print("Noo!!")

def change_tuple(tup):
    new_arr = []
    for item in tup:
        if (item % 2 == 0):
            new_arr.append(item)
    new_tup = tuple(new_arr)
    return new_tup


new_tuple = change_tuple(my_tuple)
print(type(new_tuple))
print(new_tuple)
picture = [
    [0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for i in picture:
    for j in i:
        if (j == 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# program to remove all the duplicates and return the modified array
my_arr = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
n = len(my_arr)
toReturn = []
for i in range(0, n):
    ele = my_arr[i]
    for j in range(i+1, n):
        if (my_arr[j] == ele):
            my_arr[j] = ""

for i in range(0, n):
    if (my_arr[i] != ""):
        toReturn.insert(i, my_arr[i])
print(toReturn)
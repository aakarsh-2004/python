new_list = ["a", "b", "c"]

# creating a copy of the original list, so that the original list will not get modified
my_list = new_list.copy()
# swapping the values of a list
temp_val = my_list[0]
my_list[0] = my_list[1]
my_list[1] = temp_val


# list methods
my_list.append(6)
my_list.pop()
my_list.insert(0, 1)
print(my_list.index("a"))
# clears all the element in the list
# my_list.clear()
print(my_list.count(1))
my_list.remove("a")
my_list.remove(1)
my_list.reverse()
my_list.extend(["a", "x", "t"])

# .sort() is a method for list which does not return any list, it changes the original, whereas sorted() is a function which returns another list after sorting

my_list.sort()
print(my_list)
print(sorted(my_list))


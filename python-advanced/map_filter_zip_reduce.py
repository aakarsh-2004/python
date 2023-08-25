# Importing reduce from built in python library
from functools import reduce


# Map function in python (is the same as javascript)
def mul(i):
    return i*i

# will return the squared numbers
mod_li = list(map(mul, [1, 2, 3])) #does not modify the og list

print(mod_li)



# Filter function (same as js)
def fil(item):
    return item % 2 == 0

mod_li_two = list(filter(fil, [1, 2, 3]))
print(mod_li_two) # returns 2



# Zip function (specifically in python)
# This function takes two lists or more and takes elements of each of the list and append them into a new list
list_one = [1, 2, 3]
list_two = [4, 5, 6]
mod_li_three = list(zip(list_one, list_two))
print(mod_li_three) 






# Reduce function (same as js)
# item me iterable object ki value ayegi or i me jo item ke pehle value thi wo ayegi
def red(i, item):
    return i + item # i is used as the secondary value for prev info

lis_one = [1, 2, 3, 4, 5, 6]
res = reduce(red, lis_one, 0) # 0 is i here
print(res) # prints 21
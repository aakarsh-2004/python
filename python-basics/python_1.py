import random as rn
import sys
import time as tm

class test_class:
    def __init__(self) -> None:
        pass
    def my_func(name):
        return f"Heyy, {name}"
    def guess_number():
        # randint includes upper and lower case arguments but do not support step like randrange
        guess = rn.randint(0, 10)
        return guess

print(test_class.my_func("Aakarsh"))
print(test_class.guess_number())

# Handling low level things in python by using sys module's functions
sys.stdout.write("Hemlo!") # doesn't automatically add a new line
print()
curr_time = "%H:%M:%S"
# Returns the current local time as string
print(tm.strftime(curr_time))

# getting binary of the number
print(bin(5))
# getting the number from the binary, here 2 is mandatory
print(int('0b101', 2))

# In python if we want to tell other programmers if a particular variable is a constant we make it in all CAPS.

PI = 3.14
# though we can change it, but it is the standard naming convention for constant variables in python


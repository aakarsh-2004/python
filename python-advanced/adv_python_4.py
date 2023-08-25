def sum(num1, num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func(num1, num2)

print(sum(10,20))



# docstrings are very useful in python, we can know about the function with docstrings

def test(a):
    '''
    Info: this function tests and print param a
    '''
    print(a)

test("aakarsh")
# we can read about the function
help(test)

# does the same thing as help function
print(test.__doc__)
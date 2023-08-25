def highest_even(li):
    max_val = 0
    for i in li:
        if (i % 2 == 0) and (i > max_val):
            max_val = i
        else:
            pass
    return max_val

print(highest_even([10, 2, 3, 4, 8, 11]))



# Scopes in python
x = 10
def func():
    # This actually changes the variable x that is defined outside the func
    global x
    x += 20
    print(f"value of x inside the function {x}")
func()
print(f"value of x outside the function {x}")


def test():
    y = 4
    def inner():
        # nonlocal and global are similar, just the nonlocal keyword is not just limited to global vars, it can check any indented parent elements
        nonlocal y
        return y
    return inner()

print(test())

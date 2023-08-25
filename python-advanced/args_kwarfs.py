def is_even(num):
    # using ternary operator
    return True if (num % 2 == 0) else False

print(is_even(5))


# We can take args to take unlimited arguments like this and kwargs is used to define keyword arguments meaning if we give some keyword/named arguments when calling the function, all of them will get stored in kwargs
def add(*args, **kwargs):
    total = 0
    # we get kwargs as dictionary
    # print(kwargs)
    for items in kwargs.values():
        total += items
    total += sum(args)
    return total

print(add(5, 12, 2, 10, n1 = 10, n2 = 3))

#Rule: params, *args, default params, **kwargs
def geometric_mean(a, b):
    mean = (a * b) / (a + b)
    return int(mean)

my_var = geometric_mean(10, 12)
print(my_var)


# If we want to give unlimited arguments and parameters we can use * notation

def average_sum(*numbers): # we convert the parameters to tuple making it unlimited
    sum = 0
    for item in numbers:
        sum += item
    return (sum) / len(numbers)

result = average_sum(1, 2, 3, 4)
print(result)


# To make parameters as dictionary we can use ** before argument definition

def name(**name):
    print("Hemlo,", name["fname"], name["lname"])

name(fname = "Aakarsh", lname = "Beohar")

greeting = "Hemlo, {0}. Wassup bitch ass? I am from {1}!!"
country= "India"
name = "Aakarsh"

my_greet = greeting.format(name, country)

print(my_greet)

# We can make it more simpler

greeting = f"Hemlo, my name is {name}, I am from {country}"
print(greeting)

price = 3.132112

print(f"The final price of the product is $ {price:.3}")
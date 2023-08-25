import time

# user_input = int(input("Enter a number: "))

# if (user_input >= 18):
#     print("Eligible to drive!!")
# elif (user_input == 20):
#     print("Cheers to 20s!!")
# else:
#     print("Not eligible to drive")



# Classes are so easy to construct in python

class Constructor:
    def __init__(self) -> None:
        pass
    def my_name(name):
        return f"Hemlo {name}"

greetings = Constructor.my_name('Aakarsh')
print(greetings)




# Playing with time

timestamp = time.strftime('%H:%M:%S')
timestamp_hour = int(time.strftime('%H'))


if (timestamp_hour > 4 and timestamp_hour < 12):
    print("Good Morning!")
elif (timestamp_hour >= 12 and timestamp_hour < 16):
    print("Good Afternoon!")
elif (timestamp_hour >= 16 and timestamp_hour < 3):
    print("Good Evening!")
else:
    print("Incorrect date")


# if (timestamp > 12):
#     print("Good Afternoon!")


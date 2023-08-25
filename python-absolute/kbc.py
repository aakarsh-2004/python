import time as tm

all_questions = {
    "first_ques": "Pokemon ke main character ka name kya hai?"
}

name = input("Enter your name => ")
def greeting(name):
    curr_hour = int(tm.strftime("%H"))
    greeting = ""

    if (curr_hour >= 4 and curr_hour < 12):
        greeting = "Hello, Good Morning " + name + "!!"
    elif (curr_hour >= 12 and curr_hour < 16):
        greeting = "Hello, Good Afternoon " + name + "!!"
    else:
        greeting = "Hello, Good Evening " + name + "!!"
    
    print(greeting)

greeting(name)

print("Adab Abhinandan Aadar \nWelcome to Kaun Banega Crorepati!!")
print("To play please enter start")

user_input = input("Type start or s to beging => ").lower()

if (user_input == "start" or "s"):
    print(all_questions["first_ques"])
    print("Your options are \n A) Ash \n B) Eren \n C) Mikasa \n D) Lelouch")
    user_ans = input("Enter your answer => ").lower()
    if (user_ans == 'ash' or 'a'):
        print("You got it, congrats!!")
    else:
        print("Try Again!")

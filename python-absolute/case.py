user_input = input("Enter an alphabet: ")

match user_input.lower():
    case 'a':
        print("ok!")
    case 'b':
        print("ok b!")
    case _ if (user_input == 'c'): # Default cases
        print("Not a or b, bc it's c lol!")
    case _: 
        print("Not a or b or c!")
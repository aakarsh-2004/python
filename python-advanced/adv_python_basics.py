# Using ternary operator in python is kinda different
inpt = input("Enter a alphabet => ") or "a"
cond = "got it!" if inpt == "a" else "nope"

print(cond)

# Using switch case in python

match(inpt):
    case 'a':
        print("okie")
    case 'b':
        print('bkie')
    case _:
        print("default case")
        


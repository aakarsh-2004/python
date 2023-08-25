# We don't have to really give variable names in python when using loops
for _ in range(10):
    print(_)

print(list(range(10)))


# enumerate function
# the function takes generally two variables, one is used to display the index and another is used to display the actually value at that index inside the enumerate function
for i,char in enumerate("heyy"):
    print(i, char)
# the output will be
'''
0 h
1 e
2 y
3 y
'''

# Printing the value at index 40 using enumerate 
for i, ele in enumerate(list(range(0, 100, 2))):
    if (i == 40):
        print(ele)
        break

while True:
    print("Inga Pinga Pode tumri amma ke lode")
    break
else:
    print("Inga pinga na pode")

# If I add a else block with while or for loop, it will execute after the loop has been successfully completed, it won't get executed if something like a break statement is used


#age = int(input("How old are you?\n"))

#if age >= 16 and age <= 65:

# x = input("Please enter some text for x")
# y = input("Please enter some text for y")
#
# if x:
#     print("Some text entered for x")
# if not x:
#     print("Some text entered for y")

# parrot = "Norwegian blue"
# letter = input("Please, enter a letter")
#
# if letter in parrot:
#     print("I would need that {} letter".format(letter))
# else:
#     print("Thanks, I don't need that one")

name = input("Please, enter your name?\n")
age = int(input("Nice to meet you, {}. How old are you?\n".format(name)))

if 18 <= age <= 30:
    print("Welcome, to the party, {}!".format(name))
else:
    print("Sorry, {}, this party only for young people!".format(name))
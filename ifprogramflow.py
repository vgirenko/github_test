# name = input("Please, Enter your name:"'\n')
# age = int(input("How old are you, {0}?\n".format(name)))
#
#
# if age >=18:
#     print("You are old enough to get drunk")
#
# else:
#     print("You are too young to get drunk, my friend. Just wait some {0} years.".format(18-age))

print("Please, get the number between 1 and 10")
guess = int(input())

if guess < 5:
    print("Please, get higher number")
    guess = int(input())
    if guess == 5:
        print("Great! Correct!")
    else:
        print("Your guess is incorrect")
elif guess > 5:
    print("Please, get lower number")
    guess = int(input())
    if guess == 5:
        print("Great job! That is correct!")
    else:
        print("Mistake! You are useless, motherfucker")
else:
    print('You did it from the first time! Unbelievable')
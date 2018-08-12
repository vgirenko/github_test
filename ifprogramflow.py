# name = input("Please, Enter your name:"'\n')
# age = int(input("How old are you, {0}?\n".format(name)))
#
# if age >= 18:
#     print("You are old enough to get drunk")
#
# else:
#     print("You are too young to get drunk, my friend. Just wait some {0} years.".format(18 - age))
#
# print("")

# guess = int(input("Please, get the number between 1 and 10:\n"))
#
# if guess < 5:
#     guess = int(input("I'm afraid you wrong, try higher:\n"))
#     if guess == 5:
#         print("Great! Correct!")
#     else:
#         print("Your guess is incorrect")
# elif guess > 5:
#     guess = int(input("I'm afraid you wrong, try lower:\n"))
#     if guess == 5:
#         print("Great job! That is correct!")
#     else:
#         print("Mistake! You are useless, motherfucker")
# else:
#     print('You did it from the first time! Unbelievable')


# guess = int(input("Please, guess a number from 1 to 10:\n"))
#
# if guess > 5:
#     guess = int(input("To high, please, try lower:\n"))
#     if guess == 5:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess < 5:
#     guess = int(input("To low, please, guess higher:\n"))
#     if guess == 5:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("Great work! You guessed it from the first time!")
#
#  We can make this code much simpler and more efficient


guess = int(input("Please, guess a number from 1 to 10:\n"))

if guess != 5:
    if guess < 5:
        print("Please, guess higher")
    else:  # guess must be greater than 5
        print("Please, guess lower")

    guess = int(input())
    if guess == 5:
        print("Great job! Guessed!")
    else:
        print("Sorry, you haven't guessed correctly")
else:
    print("Good! The first time!")

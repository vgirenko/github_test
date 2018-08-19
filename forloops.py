for i in range(1, 20):
    print("I is now {}".format(i))

# number = "883,44,335,600,4564,3,55"
# for i in range(0, len(number)):
#     print(number[i])  # by using square bracket it print the character at position I

# number = "883,44,335,600,4564,3,55"
# for i in range(0, len(number)):
#     if number[i] in '0123456789':  # display only numbers, without separators
#         print(number[i], end='')  # using square bracket print the character at position I. end ='' change \n to space

number = "883,44,335,600,4564,3,55"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':  # display only numbers, without separators
        cleanedNumber = cleanedNumber + number[i]  # number is a string. To perform math, convert to int with extra var
#        print(number[i], end='')  # using square bracket print the character at position I. end ='' change \n to space

newNumber = int(cleanedNumber)  # in first block we got rid off strings and assign string numbers to new variable
print("The number is {}".format(newNumber))  # in second block we converted our digits into the int format

number = "9,223,555,475,376,453"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # cleanedNumber = cleanedNumber + number[i]
        cleanedNumber += number[i]  # Augmented assignment
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

x = 23
x *= 3

print(x)

x -= 4
print(x)

x += 5
print(x)

x %= 3
print(x)

greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number

    print(answer)

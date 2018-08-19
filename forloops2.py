number = "883,44,335,600,4564,3,55"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0, 20, 4):  # 4 is a step
    print(i)

for i in range(1, 11):
    for j in range(1,11):
        print("{1} times {0} is {2} ".format(i, j, i*j))
    print("============")


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
 Public Order, Irrigation, Roads, the Fresh-Water System,
 and Public Health, what have Romans ever done for us?"""
for char in quote:
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(char, end='')

for i in range (0, 100, 7):
    print(i)

for i in range(100)[::7]:
    print(i,end='')


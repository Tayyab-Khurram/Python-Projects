file = open('DollarRates.txt', 'r')

lines = file.readlines()

diction = {}
for line in lines:
    broken = line.split('\t')
    diction[broken[0].strip()] = broken[1].strip()

userInput = int(input('Enter the amount in Dollars : '))
print('\n\t\t\t\t\tAvailabe Options!')

[print(i) for i in diction.keys()]

print('\nThis is case sensitive!, make sure to input correct spellings!')
userChoice = input('Enter the full name in lower case! : ').title()

try:
    converted = round(float(diction[userChoice]), 2) * userInput

except KeyError as err:
    print('\nPlease Enter correct spellings or right word!\n')
    exit()

print(f'\n{userInput}$ = {converted} {userChoice}\n')

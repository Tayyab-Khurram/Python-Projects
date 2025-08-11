secret_num = 9
chances = 3

def getInput():
    while True:
        try:
            user_input = int(input("Guess: "))
            return user_input
        except ValueError:
            print("Please enter a valid number.")
    

while chances > 0:
    chances -= 1
    if getInput() == secret_num:
        print("You Won!")
        break
else:
    print("You lose")

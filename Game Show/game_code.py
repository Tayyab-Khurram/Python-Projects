def play(num):
    showQuestion(num)
    showAnswer(num)
    makeDecision(correctAnswersIndex, correctAnswers, num)


def getInput():
    while True:
        try:
            userInput = int(input("\nEnter the option(0-3): "))
            return userInput
        except ValueError:
            print("\nBehave like a banday ka puttar and enter a number, samajh aai?")


def makeDecision(correctAnswersIndex, correctAnswers, num):
    if getInput() == correctAnswersIndex[num]:
        print("\nRight Answer!")
        totalWonAmount.append(awards[num])
        print(f"You won Rs.{awards[num]}!")
        print(f"Total won amount: Rs.{sum(totalWonAmount)}\n")
        if num != len(correctAnswers) - 1:
            play(num + 1) # This thing is here to keep on moving the game forward
    else:
        print("\nWrong Answer!\nGame Over!")
        print(f"Correct Answer was: {correctAnswers[num]}\n")


def showQuestion(num):
    print(f"Q.{num+1}) {questions[num]}")


def showAnswer(ans):
    for a in range(len(answers[ans])):
        # print(f"{a})", answers[ans][a], "\t", end="")
        print(f"{a})", answers[ans][a])


questions = [
    "Who set before the Indian Muslims a national goal which later came to be known as Pakistan?\n",
    "The national sport of Pakistan is?\n",
    "Which tree is the national tree of Pakistan?\n",
    "What is the capital of Germany?\n",
    "Who is the president of America?\n",
    "Kabul River enters Pakistan near border crossing at\n",
]

answers = [
    ["Haji Shariatullah", "Rehmat Ali", "Allama Iqbal", "Quaid-e-Azam"],
    ["Cricket", "Hockey", "Football", "Squash"],
    ["Neem", "Sheeshum", "Diyodar", "Date Palm"],
    ["Frankfurt","Hamburg","Berlin","Cologne"],
    ["Obama", "Trump", "Biden", "Haris"],
    ["Khyber Pass", "Khunjerab Pass", "Kandahar-Chaman", "Torkham"],
]

awards = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000]
totalWonAmount = []
correctAnswers = ["Allama Iqbal", "Hockey", "Diyodar","Berlin", "Trump", "Torkham"]
correctAnswersIndex = [2, 1, 2, 2, 1, 3]

if __name__ == "__main__":
    num = len(questions)
    play(num - num)

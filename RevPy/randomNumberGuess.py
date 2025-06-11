import random

print("-- Welcome to Random Number Guess Game --")

randomNum = random.randint(1 , 100)
# print(f"Random Number :  {randomNum}" )


guessCount = 0

while True:
    userNum = int(input("Guess a number (1 to 100) : "))

    if userNum < 1 or userNum > 100:
        print("-- Invaild Range --")
    elif userNum > randomNum:
        guessCount += 1
        print("Your Guess is High!")
    elif userNum < randomNum:
        guessCount +=1
        print("Your Guess is Low!")
    elif userNum == randomNum:
        guessCount +=1
        print("Right Guess!")
        print(f"Guess Count : {guessCount}")
        break
    else : 
        print("Something went wrong!")
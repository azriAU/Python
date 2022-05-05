import random

number = random.randint(1, 10)

print("I am thinking of a number between 1 to 10.")

for i in range(0,3):
    count = str(3 - i)
    print("You have " + count + " remaining attempt(s)")
    guess = int(input("Guess the number: "))
    if i == 2:
        if guess == number:
            print("You guessed it!")
            break
        else:
            print("You've ran out of guesses!")
            break
    else:
        if guess == number:
            print("You guessed it!")
            break
        else:
            print("Guess again!")
import random

n = random.randint(1, 100)
guess = 0
a = None

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

while a != n:
    a = int(input("Guess the Number: "))
    guess += 1

    if a > n:
        print("Lower number please!\n")
    elif a < n:
        print("Higher number please!\n")
    else:
        print(f"🎉 You guessed it right! The number was {n}.")
        print(f"You took {guess} attempts.")

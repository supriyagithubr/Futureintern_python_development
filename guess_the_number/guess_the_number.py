import random
number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Enter the guess value:-"))

    if guess < number:
        print("computer number is", number)
        print("guess number is higher")

    elif guess > number:
        print("computer number is", number)
        print("guess number is lower")

    else:
        print("guess number is equal")

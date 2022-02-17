import random

debug = False
rRange = [1,100]
closeRange = 10
allowedTries = 10
percentage = 100
tries = 1
rNumber = random.randrange(*rRange)

difficulty = {
    "easy": [1,10],
    "medium": [1,50],
    "hard": [1,100],
    "expert": [1,1000],
}

print(f"Guess a number from {rRange[0]} to {rRange[1]}")

while True:
    if debug:
        print(rNumber)
    
    guess = input(">")
    try:
        if not int(guess) in range(*rRange) and not isinstance(guess, int):
            print(f"Please input a valid number that is from {rRange[0]} to {rRange[1]}!")
            break
    except:
        print(f"Please input a valid number that is from {rRange[0]} to {rRange[1]}!")
        break
    
    guess = int(guess)
    
    if guess == rNumber:
        print("Your guess was correct!")
        print(f"It took you {tries} attempt(s) to guess the number {rNumber}!" if tries > 0 else "You guessed the number " +
                  f"{rNumber} on your first attempt!")
        print(f"Your score was {percentage}%!")
        break
        
    if guess < rNumber:
        if guess + closeRange > rNumber:
            print("You were too low... But you are close!")
        else:
            print("You were too low")
    else:
        if guess - closeRange < rNumber:
            print("You were too high... But you are close!")
        else:
            print("You were too high")
    
    print("Your guess was incorrect!\nPlease try again!")
    percentage = round((allowedTries - tries) / allowedTries, 1) * 100 if tries < allowedTries else 0
    # print(f"{percentage}%")
    tries += 1
    

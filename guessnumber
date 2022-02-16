import random

debug = False
rRange = [1,100]
allowedTries = 15
tries = 1
rNumber = random.randrange(*rRange)

print(f"Guess a number from {rRange[0]} to {rRange[1]}")

while tries < allowedTries:
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
        break
        
    if guess < rNumber:
        print("You were too low")
    else:
        print("You were too high")
    
    print("Your guess was incorrect!\nPlease try again!")
    tries += 1
    
    

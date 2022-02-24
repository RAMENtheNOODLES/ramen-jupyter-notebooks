from colorama import init, Fore, Back, Style, Cursor
import random
import os

max_x, max_y = os.get_terminal_size()

init(autoreset = True)

pos = lambda y, x: Cursor.POS(x, y)

print("" + pos(1, 1))

print(Fore.GREEN + "Wordle in Python! (Currently a WIP)")
print("Please guess a 5 letter word")

correct_letters = []
guessed_letters = []
prev_guesses = []
word = "start"

while True:
    print("" + pos(max_y - 1, max_x - 1))
    for i in range(len(prev_guesses)):
        print(prev_guesses[i])
    guess = input(">")
    if len(guess) != 5:
        print(Fore.RED + "Please enter a 5 letter word")
        continue
        
    if guess == word:
        print(Fore.BLUE + "You guessed the right word!")
        break
        
    temp_prev_guess = ""
    temp_guess = []
    
    for i in range(5):
        if guess[i] == word[i]:
            try:
                temp_guess.remove(guess[i])
            except:
                pass
            correct_letters.append(guess[i])
            temp_prev_guess += Fore.GREEN + guess[i]
        else:
            n = False
            for k in range(5-i):
                if guess[i] == word[k]:
                    temp_guess.append(guess[i])
                    temp_prev_guess += Fore.YELLOW + str(guess[i])
                    n = True
                    break
            if not n:
                temp_guess.append(guess[i])
                temp_prev_guess += Fore.RED + str(guess[i])
    
    prev_guesses.append(temp_prev_guess)

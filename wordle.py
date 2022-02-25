from colorama import init, Fore, Back, Style, Cursor
import random
import os

os.system("clear")

max_x, max_y = os.get_terminal_size()

init(autoreset = True)

pos = lambda y, x: Cursor.POS(x, y)

wordlist = open("wordlelist.csv", "r").read().lower().split("\n")

# print(f"Word list:\n{wordlist}")

print("" + pos(1, 1))

print(pos(1, 1) + Fore.GREEN + "Wordle in Python! (Currently a WIP)")
print("Please guess a 5 letter word")

correct_letters = []
guessed_letters = []
prev_guesses = []
word = wordlist[random.randrange(0, len(wordlist) - 1)]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# print(word)

while True:
    if len(prev_guesses) == 5:
        print(pos(5, 1) + "")
        print(f"You ran out of guesses!\nThe word was:\t{word}")
        break
        
    row = 1
    for i in range(len(alphabet)):
        print(pos(row, max_x - 9) + "")
        if correct_letters.count(alphabet[i]) > 0:
            print(pos(row, max_x - (9 * row) + i) + Fore.GREEN + alphabet[i])
        elif guessed_letters.count(alphabet[i]) > 0:
            print(pos(row, max_x - (9 * row) + i) + Fore.RED + alphabet[i])
        else:
            print(pos(row, max_x - (9 * row) + i) + Fore.WHITE + alphabet[i])
            
        if i in (8, 17):
            row += 1
    
    print("" + pos(max_y - 1, max_x - 1))
    for i in range(len(prev_guesses)):
        print(pos(round(max_y/2) + len(prev_guesses), round(max_x/2) - 5) + f"{Fore.CYAN}{i+1} " + prev_guesses[i])
        
    print(pos(max_y - 1, 1) + ">     ")
    guess = input(pos(max_y - 1, 1) + Fore.CYAN + ">" + Fore.RESET)
    
    # print("" + pos(round(max_y/2) + len(prev_guesses), round(max_x/2)) + guess)
    
    if len(guess) != 5:
        print(pos(max_y - 2, 1) + Fore.RED + "Please enter a 5 letter word")
        continue
        
    if guess == word:
        print(Fore.BLUE + "You guessed the right word!")
        break
        
    if guess not in wordlist:
        print(pos(max_y - 2, 1) + Fore.RED + "That is not a valid word       ")
        continue
        
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
                guessed_letters.append(guess[i])
                temp_prev_guess += Fore.RED + str(guess[i])
    
    prev_guesses.append(temp_prev_guess)

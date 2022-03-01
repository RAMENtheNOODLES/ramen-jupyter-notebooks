from colorama import init, Fore, Back, Style, Cursor

print("Welcome to text adventure!\nWIP")

chapters = []
c = open("story_chapters.txt")
for i in c:
    print(i)
    chapters.append(i)
    


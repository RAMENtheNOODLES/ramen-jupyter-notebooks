from colorama import init, Fore, Back, Style, Cursor

print("Welcome to text adventure!\nWIP")

chapters = []
c = open("story_chapters.txt", "r")
for i in c:
    print(i)
    chapters.append(i)
    
def read_story(chapter):
    f = open(f"{chapter}/main.txt")
    


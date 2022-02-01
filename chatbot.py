# Constants
VALID_RESPONSES = [
  [["Hello", "Hey", "Hola"], "Hi there!"],
  [["What is your name?", "What's your name?", "Name?", "Name"], "My name is Chatty, the chatbot!"]
]

def main():
  while True :
    print("Please ask a question and I'll answer it as best as I can!")
    response = input("> ")
    if response in ["quit", "q", "exit"]:
      return
    resp(response)
    
    
def resp(response):
  for i in range(len(VALID_RESPONSES)):
    for k in range(len(VALID_RESPONSES[i][0])):
      if response == VALID_RESPONSES[i][0][k]:
        print(VALID_RESPONSES[i][1])
        return
      

if __name__ == "__main__":
  main()

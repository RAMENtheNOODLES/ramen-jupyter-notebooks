from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

mybot = ChatBot(name='Chatty', read_only=False, logic_adapters=
               ['chatterbot.logic.BestMatch'])

small_talk = [
  'Hi there!',
  'How do you do?',
  'How are you?',
  'What\'s your name?',
  'I\'m cool',
  'Fine, you?',
  'I\'m okay',
  'Glad to hear that!',
  'Not so good',
  'Sorry to hear that',
  'What\'s your name?',
  'My name is Chatty the chatbot!'
]

trainer = ListTrainer(mybot)

trainer.train(small_talk)
  

while True:
    try:
        bot_input = mybot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

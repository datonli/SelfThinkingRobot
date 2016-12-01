import sys
sys.path.append("..")
from chatterbot.chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot("Charlie")

# Get a response to the input "How are you?"
response = chatbot.get_response("How are you?")

print(response)

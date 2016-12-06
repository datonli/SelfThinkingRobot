import sys
sys.path.append("..")
from chatterbot.chatterbot import ChatBot
from chatterbot.adapters.logic.closest_meaning import ClosestMeaningAdapter
import logging


'''
This is an example showing how to train a chat bot using the
Ubuntu Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Example Bot',
    trainer='chatterbot.trainers.UbuntuCorpusTrainer',
    logic_adapters=[
            'chatterbot.adapters.logic.ClosestMeaningAdapter',
            'chatterbot.adapters.logic.SentimentAdapter'
        ],
)

# Start by training our bot with the Ubuntu corpus data
chatbot.train()

# Now let's get a response to a greeting
response = chatbot.get_response('What\'s the matter with you?')
print(response)

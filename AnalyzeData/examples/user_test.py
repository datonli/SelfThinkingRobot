import sys
sys.path.append("..")
from chatterbot.chatterbot import ChatBot

chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        silence_performance_warning=True
        )

chatbot.train("chatterbot.corpus.english")
print(chatbot.get_response("Hello, how are you today?"))

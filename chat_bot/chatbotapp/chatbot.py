from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



def get_chatbot():
    bot = ChatBot("chatbot", read_only=False, logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry am not conversate with that",
            "maximum_similarity_threshold": 0.9

        }
    ]
)
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.english")
    return bot
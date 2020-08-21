from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot(
    'Clinica',
    preprocessors=[
        'chatterbot_bis.preprocessors.convert_to_ascii',
        'chatterbot_bis.preprocessors.unescape_html',
        'chatterbot_bis.preprocessors.clean_upper_case'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot_bis.comparisons.JaccardSimilarity',
            #'response_selection_method': 'chatterbot.response_selection.get_first_response',
            'default_response': 'Lo siento, pero no entiendo.',
            'maximum_similarity_threshold': 0.90
       }
    ]
)


trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('corpus_bis.clinica')

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
if __name__ == "__main__":
    app.run()

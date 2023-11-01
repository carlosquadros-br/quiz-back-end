from flask import Flask, jsonify, request
import json
import os 
from flask_cors import CORS
from question_factory import QuestionFactory

class App: 

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.question_factory = QuestionFactory()
        print(self.get_url_map())

        @self.app.route("/content")
        def content():
            data = self.getContent();
            questions = []
            for question_data in data:
                question = self.question_factory.create_question(
                    question_data['id'], 
                    question_data['nivel'], 
                    question_data['points'], 
                    question_data['category'], 
                    question_data['question'], 
                    question_data['choices']
                )
                questions.append(question.to_dict())
            return jsonify(questions)
        
        @self.app.route("/calculate-result",  methods=['POST'])
        def calculateResult(): 
            answers = request.data
            correctAnswers = 0 
            points = 0 
            return {
                points: points,
            }

    def run(self, debug=True):
        self.app.run(debug=debug)

    def getContent():
        json_url = "quiz.json"
        data = []
        with open(json_url, 'r') as f:
            data = json.load(f)
        return data

    def run(self, debug=True):
        self.app.run(debug=debug)

    def get_url_map(self):
        return self.app.url_map
    
if __name__ == '__main__':
    app = App()
    app.run(debug=True)
    print(app.get_url_map)

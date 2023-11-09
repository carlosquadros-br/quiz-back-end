from flask import jsonify
from model.choice import Choice

from model.question import Question

class QuestionFactory:
    def create_question(self, data):
    
        choices = [Choice(choice) for choice in data['choices']]
        return Question(data, choices)
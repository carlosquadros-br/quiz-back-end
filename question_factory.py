from flask import jsonify
from model.choice import Choice

from model.question import Question

class QuestionFactory:
    def create_question(self, data):
    
        choices = [Choice(c['id'], c['text'], c['is_correct']) for c in choices_data]
        return Question(
            question_data['id'], 
            question_data['nivel'], 
            question_data['points'], 
            question_data['category'], 
            question_data['question'], 
            question_data['choices']
        )
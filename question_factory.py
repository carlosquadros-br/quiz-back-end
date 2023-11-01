from flask import jsonify
from model.choice import Choice

from model.question import Question

class QuestionFactory:
    def create_question(self, id, nivel, points, category, question_text, choices_data):
        choices = [Choice(c['id'], c['text'], c['is_correct']) for c in choices_data]
        return Question(id, nivel, points, category, question_text, choices)
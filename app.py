from flask import Flask, jsonify, request
from flask_cors import CORS
from question_factory import QuestionFactory
from quiz import Quiz


app = Flask(__name__)
quiz = Quiz()
    
@app.route("/content")
def content():
    data = quiz.getContent()
    questions = []
    for question_data in data:

        question = quiz.question_factory.create_question(
            question_data['id'], 
            question_data['nivel'], 
            question_data['points'], 
            question_data['category'], 
            question_data['question'], 
            question_data['choices']
        )

        question = quiz.question_factory.create_question(question_data)

        questions.append(question.to_dict())
    return jsonify(questions)
        
@app.route("/calculate-result",  methods=['POST'])
def calculateResult(): 
    answers = request.get_json()
    correctAnswers = 0
    hardAnswers = 0
    mediumAnswers = 0
    easyAnswers = 0
    points = 0 
    data = quiz.getContent()
    questions = []
    for question_data in data:
        question = quiz.question_factory.create_question(
            question_data['id'], 
            question_data['nivel'], 
            question_data['points'], 
            question_data['category'], 
            question_data['question'], 
            question_data['choices']
        )
        questions.append(question)

    questions_dict = {question.id: question for question in questions}
    for answer in answers:
       question = questions_dict.get(answer['id'])
       if question and question.is_correct(answer['choice_selected']['id']):
            quiz.set_point_strategy(question.nivel)
            points += quiz.calculate_points()
            correctAnswers += 1
            if question.nivel == "Hard":
               hardAnswers += 1
            elif question.nivel == "Medium":
                mediumAnswers += 1
            elif question.nivel == "Easy":
                easyAnswers += 1

    return {
        "points": points,
        "correct_answers": correctAnswers,
        "hard_answers": hardAnswers,
        "medium_answers": mediumAnswers,
        "easy_answers": easyAnswers
        }

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
    print(app.get_url_map)

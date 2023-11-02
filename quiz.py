import json
from points_strategy import EasyPointsStrategy, HardPointsStrategy, MediumPointsStrategy
from question_factory import QuestionFactory

class Quiz: 

    def __init__(self):
        self.question_factory = QuestionFactory()
        self.point_strategy = None

    def run(self, debug=True):
        self.app.run(debug=debug)

    def getContent(self):
        json_url = "quiz.json"
        data = []
        with open(json_url, 'r') as f:
            data = json.load(f)
        return data

    def run(self, debug=True):
        self.app.run(debug=debug)

    def set_point_strategy(self, point_strategy):
        if(point_strategy == "Easy"):
            self.point_strategy = EasyPointsStrategy()
        elif(point_strategy == "Medium"):
            self.point_strategy = MediumPointsStrategy()
        elif(point_strategy == "Hard"):
            self.point_strategy = HardPointsStrategy()
    

    
    def calculate_points(self):
        return self.point_strategy.calculate_points()
import json
from patterns.points_strategy_pattern import EasyPointsStrategy, HardPointsStrategy, MediumPointsStrategy
from patterns.question_factory_pattern import QuestionFactory

# (1) Padrão Singleton
class Quiz: 

    _instance = None

    def __init__(self):
        self.question_factory = QuestionFactory()
        self.point_strategy = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

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
    

    
    def calculate_points(self, acerto):
        return self.point_strategy.calculate_points(acerto)
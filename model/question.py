class Question:
    def __init__(self, id, nivel, points, category, question_text, choices):
        self.id = id
        self.nivel = nivel
        self.points = points
        self.category = category
        self.question_text = question_text
        self.choices = choices

    def to_dict(self):
        # Convert choices to a list of dictionaries
        choices_dict_list = [choice.to_dict() for choice in self.choices]

        return {
            'id': self.id,
            'nivel': self.nivel,
            'points': self.points,
            'category': self.category,
            'question_text': self.question_text,
            'choices': choices_dict_list,
        }
    
    def get_correct_choice(self):
        for choice in self.choices:
            if choice.is_correct:
                return choice
    
    def is_correct(self, id_choice_selected):
        return id_choice_selected == self.get_correct_choice().id
class Question:
    def __init__(self, data, choices):
        self.id = data['id']
        self.nivel = data['nivel']
        self.points = data['points']
        self.category =  data['category']
        self.question_text = data['question_text']
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
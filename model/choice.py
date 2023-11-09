class Choice:
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.is_correct = data['is_correct']

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'is_correct': self.is_correct,
        }
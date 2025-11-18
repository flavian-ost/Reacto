class Player:
    def __init__(self):
        self.score = 0
        
    def get_score(self):
        return self.score
    
    def set_score(self, new_score):
        self.score = new_score
        return self.score
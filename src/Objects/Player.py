class Player:
    id
    score

    def __init__(self, id):
        self.id = id
        
    def score(self, new_score = 0 ):
        self.score += new_score
        return self.score
    
    def get_id():
        return id
class course:
    concentration = ""
    qscore = 0
    name = ""
    
    def __init__ (self, name, concentration, score):
        self.name = name
        self.qscore = score
        self.concentration = concentration
    
    def getName (self):
        return self.name
    def getScore(self):
        return self.qscore
    def getConcentration(self):
        return self.concentration
    
    
    
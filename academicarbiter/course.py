class course:
    concentration = ""
    #scores are either 1 or -1, its just thumbs up or down
    #difficulty, teaching, subject matter
    dScore = 0
    tScore = 0
    sScore = 0
    name = ""
    
    
    def __init__ (self, name, concentration, dscore, 
                  tscore, sscore):
        self.name = name
        self.dScore = dscore
        self.tScore = tscore
        self.sScore = sscore
        self.concentration = concentration
    
    def getName (self):
        return self.name
    def getScore(self):
        return self.qscore
    def getT(self):
        return self.tScore
    def getD(self):
        return self.dScore
    def getS(self):
        return self.sScore
    def getConcentration(self):
        return self.concentration
#defines the semester class

class semester:
    #array of courses
    courses = []
    
    def __init__(self, courses):
        self.courses = courses
        
    def getCourses(self):
        return self.courses
    
    
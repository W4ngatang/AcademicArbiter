#defines the actual algorithm

import course
import student
import semester
import data

class algorithm:
    #your info
    isemesters = []
    iconcentration = ""
    iyear = ""
    #data set
    students = []
    #these are dictionaries
    #the key is the name of the course or concentration
    #the value is the number of students in it
    allCourses = dict()
    allConcentrations = dict()
    #results
    courseRecs = dict()
    #your weights for different aspects of each course
    diff = 0
    teach = 0
    subj = 0
    
    #initialize an instance of the class
    def __init__ (self, sem, conc, year, 
                  students, concs, courses, 
                  difficulty, teaching, subject):
        self.isemesters = sem
        self.iconcentration = conc
        self.iyear = year
        self.students = students
        self.allConcentrations = concs
        self.allCourses = courses
        self.diff = difficulty
        self.teach = teaching
        self.subj = subject
    
    #go through every student and assign values for each course
    def values(self):
        for otherStudent in self.students:
            curYear = otherStudent.year
            if curYear == self.year:
                curSemesters = otherStudent.semesters
                curConc = otherStudent.concentration   
                similarity = 0
                semIndex = self.isemesters.length - 1
                
                #get all of the courses from you and from them
                mySem = self.isemesters[semIndex]
                theirSem = curSemesters[semIndex]
                myClasses = mySem.getCourses
                theirClasses = theirSem.getCourses
                
                #assign a weight for the other student's courses
                for myClass in myClasses:
                    for theirClass in theirClasses:
                        #check the name
                        if (myClass.getName == theirClass.getName):
                            #compare your scores for the class
                            classScore = 0
                            if (myClass.getT == theirClass.getT):
                                classScore += self.teach
                            if (myClass.getS == theirClass.getS):
                                classScore += self.subj
                            if (myClass.getD == theirClass.getD):
                                classScore += self.diff
                                #offset likelihood of being in the same large class
                                #by dividing by the size of the class
                                enrollment = self.allCourses[myClass.getName]
                                
                                similarity += 1 * (1 / enrollment) * (classScore / 100)

                #check for the same concentration
                if (curConc == self.concentration):
                    #find the number of students in that concentration
                    numStudents = self.allConcentrations[curConc]
                    similarity *= (1 + 1/numStudents)
                
                theirClasses = curSemesters[semIndex + 1].getCourses
                
                #add their courses to a list of recs
                for course in theirClasses:
                    if course in self.courseRecs:
                        self.courseRecs[course] += (similarity * course.getScore)
                    else:
                        self.courseRecs.update({course, similarity * course.getScore})  
                
                #remove the courses if they have already taken
                for x in self.courseRecs:  
                    for y in myClasses:
                        if x == y:
                            del self.courseRecs[x]
                                          
                #create a new sorted dictionary based on weights
                newRecs = dict()
                for x in (self.courseRecs.iterkeys()):
                    key = self.courseRecs[x]
                    if key in newRecs.keys(): 
                        newRecs[key].append(x)
                    newRecs[key] = x
                 
        return newRecs
                        
                        
                    
                
            
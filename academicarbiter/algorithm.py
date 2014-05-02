#defines the actual algorithm

import course
import student
import semester
import data_parser

class algorithm:
    #your info
    isemester = []
    iconcentration = ""
    iyear = ""
    #fall or spring semester
    semNum = 0
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
    def __init__ (self, sem, conc, year, semNum,
                  difficulty, teaching, subject,
                  students, courses, concs):
        self.isemester = sem
        self.iconcentration = conc
        self.iyear = int(year)
        self.semNum = int(semNum)
        self.students = students
        self.allConcentrations = concs
        self.allCourses = courses
        self.diff = int(difficulty)
        self.teach = int(teaching)
        self.subj = int(subject)
    
    #go through every student and assign values for each course
    def values(self):
        for otherStudent in self.students:
        #curYear = otherStudent.year
        #if curYear == self.year:
            curSemesters = otherStudent.getSemesters()
            curConc = otherStudent.getConcentration()
              
            similarity = 0
            semIndex = self.iyear * 2 + self.semNum
            
            #get all of the courses from you and from them
            numSems = len(curSemesters)
            if (numSems > semIndex + 2):
                theirSem = curSemesters[semIndex]
                myClasses = self.isemester.getCourses()
                theirClasses = theirSem.getCourses()
                
                #assign a weight for the other student's courses
                for myClass in myClasses:
                    for theirClass in theirClasses:
                        #check the name
                        print(theirClass.getName())
                        if (myClass.getName() == theirClass.getName()):
                            #compare your scores for the class
                            classScore = 0
                            if (myClass.getT() == theirClass.getT()):
                                classScore += self.teach
                            else:
                                classScore -= self.teach
                            if (myClass.getS() == theirClass.getS()):
                                classScore += self.subj
                            else:
                                classScore -= self.subj
                            if (myClass.getD() == theirClass.getD()):
                                classScore += self.diff
                            else:
                                classScore -= self.diff
                                
                                #offset likelihood of being in the same large class
                                #by dividing by the size of the class

                                enrollment = self.allCourses[myClass.getName()]
                                
                                similarity += 1 * (1 / enrollment) * (classScore / 100)
    
                #check for the same concentration
                if (curConc == self.iconcentration):
                    print("same concentration")
                    #find the number of students in that concentration
                    numStudents = self.allConcentrations[curConc]
                    similarity *= (1 + 1/numStudents)
                
                theirClasses = curSemesters[semIndex + 1].getCourses()
                
                #add their courses to a list of recs
                for course in theirClasses:
                    print(course.getName())
                    score = 0
                    score += (similarity * course.getD() * self.diff)
                    score += (similarity * course.getT() * self.teach)
                    score += (similarity * course.getS() * self.subj)
                    print(score)
                    if course in self.courseRecs:
                        self.courseRecs[course.getName()] += score
                    else:
                        self.courseRecs[course.getName()] = score 
            
            #remove the courses if they have already taken
            #for x in self.courseRecs:  
                #for y in myClasses:
                    #if x == y:
                        #del self.courseRecs[x]
                                      
        #create a new sorted dictionary based on weights
        newRecs = dict()
        keys = self.courseRecs.keys()
        print("first time")
        print(self.courseRecs)
        for x in keys:
            key = self.courseRecs[x]
            if key in newRecs.keys(): 
                newRecs[key].append(x)
            else:
                newRecs[key] = [x] 
        return newRecs
        
                        
                        
                    
                
            
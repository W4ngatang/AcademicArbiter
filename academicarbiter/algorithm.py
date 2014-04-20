#defines the actual algorithm

import course
import student
import semester
import data

class algorithm:
    isemesters = []
    iconcentration = ""
    iyear = ""
    students = []
    courseRecs = {}
    
    #initialize an instance of the class
    def __init__ (self, sem, conc, year, students):
        self.isemesters = sem
        self.iconcentration = conc
        self.iyear = year
        self.students = students
    
    #go through every student and assign values for each course
    def values(self):
        for x in self.students:
            curYear = x.year
            if curYear == self.year:
                curSemesters = x.semesters
                #curConc = x.concentration
                multiplier = 0
                semIndex = self.isemesters.length - 1
                mySem = self.isemesters[semIndex]
                theirSem = curSemesters[semIndex]
                myClasses = mySem.getCourses
                theirClasses = theirSem.getCourses
                for i in myClasses:
                    for j in theirClasses:
                        if (i.getName == j.getName):
                            multiplier += 1
                theirClasses = curSemesters[semIndex + 1].getCourses
                for course in theirClasses:
                    if course in self.courseRecs:
                        self.courseRecs[course] += multiplier
                    else:
                        self.courseRecs.update({course, multiplier})   
        return self.courseRecs
                        
                        
                    
                
            
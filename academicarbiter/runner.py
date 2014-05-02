import algorithm
import data_parser
import course
import semester

#take user input for course and reformat it
def clean(value):
    value = value.lower()
    value = value.replace(" ","")
    return value

#run the algorithm
def run(sD):
    #organize the course info for the user
    course1 = course.course(clean(sD[3]),sD[4],sD[5],sD[6])
    course2 = course.course(clean(sD[7]).lower(),sD[8],sD[9],sD[10])
    course3 = course.course(clean(sD[11]).lower(),sD[12],sD[13],sD[14])
    course4 = course.course(clean(sD[15]).lower(),sD[16],sD[17],sD[18])
    courses = [course1,course2,course3,course4]
    sem = semester.semester(courses)
    
    #get the data from the database
    students = data_parser.getStudents()
    courseData = data_parser.getCourses()
    concentrations = data_parser.getConcentrations()
    
    #run the algorithm
    alg = algorithm.algorithm(sem,sD[0],sD[1],sD[2],
                              sD[19],sD[20],sD[21],
                              students, courseData, concentrations)
    recs = alg.values()
    
    #get a sorted list of the courses by their weights
    keys = sorted(recs.keys(), reverse=True)
    #number of courses to return
    numWanted = 10
    totalRecs = 0
    #list of recommended courses
    recList = []

    #loop through rec dictionary to get courses
    for key in keys:
        if (totalRecs >= numWanted):
            break
        else:
            #check for length in case >1 course has the same value
            length = len(recs[key])
            for i in range(0, length):
                if (totalRecs >= numWanted):
                    break
                else:
                    recList.append(recs[key][i])
                    totalRecs += 1
    return recList

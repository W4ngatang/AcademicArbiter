#returns a list of student objects after parsing through the student database and creating the objects
import course
import student
import semester


def getStudents() :
    students = []
    dump = []
    with open("sample_students.txt") as file:
        for line in file:
            currentline = (line.rstrip("\n")).split(", "),
            dump.append(currentline)
    
    # go over the rows of the data dump
    for x in range(len(dump)):
        # if the current row's first term is 0, it's a new student so create a new student object
        if (dump[x][0][0] == "0"):
            new_semesters = []
            # variable to track when to stop adding data to the new student object
            y = 1
            curCourses = []
            while ((x+y) < len(dump) and dump[x+y][0][0] != "0"):
                # variable for modding over list
                curCourses = []
                for z in range(int((len(dump[x+y][0]) - 1) / 4)):
                    curCourses.append(
                            course.course(dump[x+y][0][4 * z + 1], 
                                          int(dump[x+y][0][4 * z + 2]), 
                                          int(dump[x+y][0][4 * z + 3]), 
                                          int(dump[x+y][0][4 * z + 4])))
                sem = semester.semester(curCourses)
                new_semesters.append(sem)
                y = y + 1
                
            new_student = student.student(dump[x][0][2], new_semesters, dump[x][0][1], "")
            students.append(new_student)
    return students

#returns a dictionary of course number, enrollment
def getCourses() :
    courses = dict()
    with open("course_data.txt") as file:
        for line in file:
            currentline = line.split(","),
            lineLength = len(currentline[0])
            if lineLength > 1:
                courses[currentline[0][0]]= int(currentline[0][1])
    return courses

#returns a dictionary of concentration, concentration
def getConcentrations() :
    concentrations = dict()
    with open("sample_concentrations.txt") as file:
        for line in file:
            currentline = line.split(", "),
            lineLength = len(currentline[0])
            if lineLength > 1:
                concentrations[currentline[0][0]]= int(currentline[0][1])
    return concentrations

getStudents()

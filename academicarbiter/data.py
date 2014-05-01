#returns a dictionary of course number, enrollment
def getCourses() :
    courses = dict()
    with open("sample_database.txt") as file:
        for line in file:
            currentline = line.split(", "),
            courses[currentline[0][0]]= currentline[0][3]
    return courses
#returns a dictionary of concentration, concentration
def getCourses() :
    concentrations = dict()
    with open("sample_concentrations.txt") as file:
        for line in file:
            currentline = line.split(", "),
            concentrations[currentline[0][0]]= currentline[0][1]
    return concentrations
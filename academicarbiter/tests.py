import semester

stuff = dict()
#stuff.update({3, "item three"})
#stuff.update({4, "item four"})
#stuff[6] = "a"
#stuff[4] = "b"
#stuff[242] = "c"
#stuff[10] = 10

#sorted(stuff, key=stuff.get)

#keys = stuff.keys()
#keys.sort()
#print (sorted(keys, reverse=True))

#stuff[10] += 10
#stuff[20] = [10,20]
#stuff[20].append(2)

#print (stuff[10])
#print (stuff[20])

stuff["a"] = 13
stuff["b"] = 14
stuff["c"] = 13
stuff["d"] = 32
stuff["e"] = -2

newStuff = dict()
for x in (stuff.keys()):
    key = stuff[x]
    if key in newStuff.keys(): 
        newStuff[key].append(x)
    else: 
        newStuff[key] = [x]
totalRecs = 0
recList = []
newKeys = sorted(newStuff.keys(), reverse=True)
    #recList.append(newStuff[newKeys[totalRecs]])
numWanted = 3

for key in newKeys:
    if (totalRecs >= numWanted):
        break
    else:
        length = len(newStuff[key])
        for i in range(0, length):
            if (totalRecs >= numWanted):
                break
            else:
                recList.append(newStuff[key][i])
                totalRecs += 1

#print (recList)

courses = ["a","b"]
sem = semester.semester(courses)
#print (sem.getCourses())
def clean(value):
    value = value.lower()
    value = value.replace(" ","")
    return value

value = "A B"

print(clean(value))
    


from Tkinter import *
import tkFont
import tkMessageBox

import runner

#define root
root = Tk()
root.withdraw()

#root.title("Course Recommendation1")
root.geometry("450x300+200+200")

#current window
windows = []

#initialize fonts
customFont = tkFont.Font(family="Helvetica", size=17)
customFont2 = tkFont.Font(family="Helvetica", size=11)

#initialize int variables for radio buttons
radio_year = IntVar()
radio_sem = IntVar()
radio_diff1 = IntVar()
radio_matrl1 = IntVar()
radio_teach1 = IntVar()
radio_diff2 = IntVar()
radio_matrl2 = IntVar()
radio_teach2 = IntVar()
radio_diff3 = IntVar()
radio_matrl3 = IntVar()
radio_teach3 = IntVar()
radio_diff4 = IntVar()
radio_matrl4 = IntVar()
radio_teach4 = IntVar()

#initializers to None
concentration = None
conc_entry = None

year_entry = None
sem_entry = None

nextdifficulty = None
nextdifficulty_entry = None

nextteaching = None
nextteaching_entry = None

nextmaterial = None
nextmaterial_entry = None

course1 = None
course1_entry = None

difficulty1 = None
material1 = None
teaching1 = None

course2 = None
course2_entry = None

difficulty2 = None
material2 = None
teaching2 = None

course3 = None
course3_entry = None

difficulty3_entry = None
material3_entry = None
teaching3_entry = None

course4 = None
course4_entry = None

difficulty4_entry = None
material4_entry = None
teaching4_entry = None


def close_window():
    window = windows[0]
    window.destroy()
    windows.remove(window)
    if not windows: root.quit()
    
def diff_var(wdw, num):
    #variable for difficulty
    var = StringVar()
    label_descr = "Difficulty of the above class:"
    var.set (label_descr)
    label = Label( wdw, textvariable=var, relief=RAISED )
    label.pack()
    
    variableName = 'radio_diff' + str(num)
    commandName = 'sel_diff' + str(num)
    
    #R6 = Radiobutton(wdw, text="Easy", variable=variableName, 
    #                 value=1,command=commandName)
    #R6.pack( anchor = W )
    #R7 = Radiobutton(wdw, text="Difficulty", variable=variableName, 
    #                 value=(-1),command=commandName)
    #R7.pack( anchor = W )
 
def teach_var(wdw):   
    # variable for teaching
    var = StringVar()
    label_descr = "Did you like or dislike the teaching of the course?"
    var.set (label_descr)
    label = Label( wdw, textvariable=var, relief=RAISED )
    label.pack()
  
def mat_var(wdw):  
    #variable for material
    var = StringVar()
    label_descr = "Did you like or dislike the material?"
    var.set (label_descr)
    label = Label( wdw, textvariable=var, relief=RAISED )
    label.pack()

def new_window():
    wdw = Toplevel()
    wdw.protocol('WM_DELETE_WINDOW', close_window)
    windows.append(wdw)
    return wdw

def main():
    first_window()
   
def first_window():
    wdw = new_window()
    #Add Welcome
    text = Text(wdw, width=45, height=1, font=customFont, bg='red')
    text.pack()
    text.insert("end","WELCOME!!")
    text.tag_config("center", justify="center")
    text.tag_add("center", 1.0, "end")

    #start the middle description    
    text = Text(wdw, width=30, height=5, font=customFont2, wrap=WORD)
    text.pack()

    descr = "Get your next semester's course recommendation based on\
 what student like you have taken in past years."
    text.insert("end",descr)
    text.config(state=DISABLED)

    #add button
    btn = Button(wdw, text ="Click to Start", command = sec_window)
    btn.pack()
   
def sec_window():
    global nextteaching_entry
    global nextmaterial_entry
    global nextdifficulty_entry
    global conc_entry
    
    #second window
    wdw = new_window()
    
    #close first window
    close_window()

    #year label
    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )

    var.set("What year are you?")
    label.pack()
    
    #add radio buttons 

    R1 = Radiobutton(wdw, text="Freshman", variable=radio_year, value=1,
                      command=sel_yr)
    R1.pack( anchor = W )
    
    R2 = Radiobutton(wdw, text="Sophomore", variable=radio_year, value=2,
                      command=sel_yr)
    R2.pack( anchor = W )

    R3 = Radiobutton(wdw, text="Junior", variable=radio_year, value=3,
                      command=sel_yr)
    R3.pack( anchor = W)

    R4 = Radiobutton(wdw, text="Senior", variable=radio_year, value=4,
                      command=sel_yr)
    R4.pack( anchor = W)


    #semester label
    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    var.set("Are you currently enrolled in Fall or Spring semester?")
    label.pack()

    #add radio button for semester
    R5 = Radiobutton(wdw, text="Fall", variable=radio_sem, value=1,
                      command=sel_sem)
    R5.pack( anchor = W )
    
    R6 = Radiobutton(wdw, text="Spring", variable=radio_sem, value=2,
                      command=sel_sem)
    R6.pack( anchor = W )
    

    #another label for concentration
    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    var.set("Enter your current/expected concentration.")
    label.pack()

    #entry field for concentration
    
    conc_entr = Entry(wdw, bd =5)
    conc_entr.pack()
    conc_entry = conc_entr

    #another label for next semester expectation
    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    description = "What do you want your next semester to be like \
in terms of the following? Give your answer on a scale of 1 to 100."
    var.set(description)
    label.pack()

    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    description = "Difficulty:"
    var.set(description)
    label.pack()

    difficulty_entr = Entry(wdw, bd =5)
    difficulty_entr.pack()
    nextdifficulty_entry = difficulty_entr

    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    description = "Material:"
    var.set(description)
    label.pack()

    material_entr = Entry(wdw, bd =5)
    material_entr.pack()
    nextmaterial_entry = material_entr

    var = StringVar()
    label = Label( wdw, textvariable=var, relief=RAISED )
    description = "Teaching:"
    var.set(description)
    label.pack()

    teaching_entr = Entry(wdw, bd =5)
    teaching_entr.pack()
    nextteaching_entry = teaching_entr

    #Add "Go to Next page" button
    btn = Button(wdw, text ="Go to Next Page.", command = third_window)
    btn.pack()

def third_window():
    global nextdifficulty
    global nextmaterial
    global nextteaching
    global concentration
    global course1_entry
    global course2_entry
    #third window
    wdw = new_window()
    #to access concentration

    nextteaching = nextteaching_entry.get()

    nextmaterial = nextmaterial_entry.get()

    nextdifficulty = nextdifficulty_entry.get()
    
    concentration = conc_entry.get()
    #close second window
    close_window()
    
    #label for courses
    var = StringVar()
    label_descr = "List the four courses that you took last semester, and \
tell us what you felt about each class."
    var.set (label_descr)
    label = Label( wdw, textvariable=var, relief=RAISED )
    label.pack()

    #four courses and the required data for each course
    course1_entr = Entry(wdw, bd =5)
    course1_entr.pack()
    course1_entry = course1_entr
    
    diff_var(wdw, 1)
    
    R6 = Radiobutton(wdw, text="Easy", variable=radio_diff1, 
                     value=1,command=sel_diff1)
    R6.pack( anchor = W )
    R7 = Radiobutton(wdw, text="Difficult", variable=radio_diff1, 
                     value=(-1),command=sel_diff1)
    R7.pack( anchor = W )

    mat_var(wdw)

    R8 = Radiobutton(wdw, text="Liked", variable=radio_matrl1, value=1,
                      command=sel_matrl1)
    R8.pack( anchor = W )
    R9= Radiobutton(wdw, text="Disliked", variable=radio_matrl1, value= -1,
                      command=sel_matrl1)
    R9.pack( anchor = W )

    teach_var(wdw)

    R10 = Radiobutton(wdw, text="Liked", variable=radio_teach1, value=1,
                      command=sel_teach1)
    R10.pack( anchor = W )
    R11 = Radiobutton(wdw, text="Disliked", variable=radio_teach1, value=-1,
                      command=sel_teach1)
    R11.pack( anchor = W )
    
    course2_entr = Entry(wdw, bd =5)
    course2_entr.pack()
    course2_entry = course2_entr
    
    diff_var(wdw, 2)
    
    R12 = Radiobutton(wdw, text="Easy", variable=radio_diff2, 
                     value=1,command=sel_diff2)
    R12.pack( anchor = W )
    R13 = Radiobutton(wdw, text="Difficult", variable=radio_diff2, 
                     value=(-1),command=sel_diff2)
    R13.pack( anchor = W )

    mat_var(wdw)

    R14 = Radiobutton(wdw, text="Liked", variable=radio_matrl2, value= 1,
                      command=sel_matrl2)
    R14.pack( anchor = W )
    R15 = Radiobutton(wdw, text="Disliked", variable=radio_matrl2, value= -1,
                      command=sel_matrl2)
    R15.pack( anchor = W )

    teach_var(wdw)

    R16 = Radiobutton(wdw, text="Liked", variable=radio_teach2, value=1,
                      command=sel_teach2)
    R16.pack( anchor = W )
    R17 = Radiobutton(wdw, text="Disliked", variable=radio_teach2, value=-1,
                      command=sel_teach2)
    R17.pack( anchor = W )

    #Add "Add info for two more courses" button
    btn = Button(wdw, text ="Add info for two more courses!", command = fourth_window)
    btn.pack()

def fourth_window ():
    global course1
    global course2
    global course3_entry
    global course4_entry
    global course3
    global course4

    course1 = course1_entry.get()
    
    course2 = course2_entry.get()

    wdw = new_window()
    
    #close third window
    close_window()
    
    
    course3_entr = Entry(wdw, bd =5)
    course3_entr.pack()
    course3_entry = course3_entr

    diff_var(wdw, 3)
    
    R6 = Radiobutton(wdw, text="Easy", variable=radio_diff3, 
                     value=1,command=sel_diff3)
    R6.pack( anchor = W )
    R7 = Radiobutton(wdw, text="Difficult", variable=radio_diff3, 
                     value=(-1),command=sel_diff3)
    R7.pack( anchor = W )

    mat_var(wdw)

    R20 = Radiobutton(wdw, text="Liked", variable=radio_matrl3, value= 1,
                      command=sel_matrl3)
    R20.pack( anchor = W )
    R21 = Radiobutton(wdw, text="Disliked", variable=radio_matrl3, value= -1,
                      command=sel_matrl3)
    R21.pack( anchor = W )

    teach_var(wdw)

    R22 = Radiobutton(wdw, text="Liked", variable=radio_teach3, value= 1,
                      command=sel_teach3)
    R22.pack( anchor = W )
    R23 = Radiobutton(wdw, text="Disliked", variable=radio_teach3, value= -1,
                      command=sel_teach3)
    R23.pack( anchor = W )
    
    course4_entr = Entry(wdw, bd =5)
    course4_entr.pack()
    course4_entry = course4_entr
    
    diff_var(wdw, 4)
    
    R24 = Radiobutton(wdw, text="Easy", variable=radio_diff4, 
                     value=1,command=sel_diff4)
    R24.pack( anchor = W )
    R25 = Radiobutton(wdw, text="Difficult", variable=radio_diff4, 
                     value=(-1),command=sel_diff4)
    R25.pack( anchor = W )

    mat_var(wdw)

    R26 = Radiobutton(wdw, text="Liked", variable=radio_matrl4, value= 1,
                      command=sel_matrl4)
    R26.pack( anchor = W )
    R27 = Radiobutton(wdw, text="Disliked", variable=radio_matrl4, value= -1,
                      command=sel_matrl4)
    R27.pack( anchor = W )

    teach_var(wdw)

    R28 = Radiobutton(wdw, text="Liked", variable=radio_teach4, value= 1,
                      command=sel_teach4)
    R28.pack( anchor = W )
    R29 = Radiobutton(wdw, text="Disliked", variable=radio_teach4, value= -1,
                      command=sel_teach4)
    R29.pack( anchor = W )
    


    #Add "get recommendations" button
    btn = Button(wdw, text ="GET RECOMMENDATIONS!", command = get_reco)
    btn.pack()


def get_reco():
    global course3
    global course4

    course3 = course3_entry.get()

    course4 = course4_entry.get()
    
    data = [concentration,year_entry,sem_entry,
            course1,int(difficulty1),int(teaching1),int(material1),
            course2,int(difficulty2),int(teaching2),int(material2),
            course3,int(difficulty3),int(teaching3),int(material3),
            course4,int(difficulty4),int(teaching4),int(material4),
            int(nextdifficulty),int(nextteaching),int(nextmaterial)]
    
    courses = runner.run(data)
    
    fifth_window(courses)

#fifth_window
def fifth_window(courses):
    wdw = new_window()
    
    #close third window
    close_window()

    #course recommendations:
    text = Text(wdw, width=45, height=1, font=customFont, bg='red')
    text.pack()
    text.insert("end","Here are some recommended courses for you:")
    text.tag_config("center", justify="center")
    text.tag_add("center", 1.0, "end")
    text.config(state=DISABLED)
    print(courses)
    print(len(courses))

    for i in range (0, 9):

        #List of course recommendations based on the algorithms will go here:
        var = StringVar()
        label_descr = courses[i]
        var.set (label_descr)
        label = Label( wdw, textvariable=var, relief=RAISED )
        label.pack()

    #Add "Start All Over again" button
    btn = Button(wdw, text ="Go back to Home Page!", command = sec_window)
    btn.pack()
    

def sel_yr():
    global year_entry
    year_entry = str(radio_year.get())
    
def sel_sem():
    global sem_entry
    sem_entry = str(radio_sem.get())

def sel_diff1():
    global difficulty1
    difficulty1 = str(radio_diff1.get())

def sel_matrl1():
    global material1
    material1 = str(radio_matrl1.get())

def sel_teach1():
    global teaching1
    teaching1 = str(radio_teach1.get())

def sel_diff2():
    global difficulty2
    difficulty2 = str(radio_diff2.get())

def sel_matrl2():
    global material2
    material2 = str(radio_matrl2.get())

def sel_teach2():
    global teaching2
    teaching2 = str(radio_teach2.get())

def sel_diff3():
    global difficulty3
    difficulty3 = str(radio_diff3.get())

def sel_matrl3():
    global material3
    material3 = str(radio_matrl3.get())

def sel_teach3():
    global teaching3
    teaching3 = str(radio_teach3.get())

def sel_diff4():
    global difficulty4
    difficulty4 = str(radio_diff4.get())

def sel_matrl4():
    global material4
    material4 = str(radio_matrl4.get())

def sel_teach4():
    global teaching4
    teaching4 = str(radio_teach4.get())
    

    
main()
root.mainloop()

from Tkinter import *
import tkFont
import tkMessageBox


root = Tk()
root.withdraw()

#root.title("Course Recommendation1")
root.geometry("450x300+200+200")

#current window
windows = []

customFont = tkFont.Font(family="Helvetica", size=17)
customFont2 = tkFont.Font(family="Helvetica", size=11)

#root is first window
#current_frame = None
radio_var = IntVar()

course_entries = []
conc_entry = None


def close_window():
    window = windows[0]
    window.destroy()
    windows.remove(window)
    if not windows: root.quit()

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
    text.config(state=DISABLED)

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

# TODO   
def sec_window():
    print "TODO"

main()
root.mainloop()

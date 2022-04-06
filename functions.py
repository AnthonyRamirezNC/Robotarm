from tkinter import *

from tkinter.ttk import *

from servologic import *

#create screen object
Window = Tk()

#setting screen size
Window.geometry('700x300')


#creating text box
def textbox():    
    my_text_box = Text(Window,height=5, width = 10)
    my_text_box.pack()
    submit(my_text_box)
    return my_text_box

#getting user input
def getInput(my_text_box):
    angle = my_text_box.get("1.0","end-1c")
    #what to do with input after submitting, can add functions here
    servochoice = getmenu()
    useangle(int(angle),servochoice)

#create button for Submitting info
def submit(my_text_box):
    submitch = Button(Window, text = "Submit",command =lambda: getInput(my_text_box))
    submitch.pack()

#creating dropdown menu
menu = StringVar()
menu.set("Select motor")

#motor selection
def motorselect():
    mtrselection = OptionMenu(Window, menu,"Select Motor","Waist","Lower Arm", "Upper Arm", "Wrist","Wrist Rotation")
    mtrselection.pack()
    textbox()

#get menu function
def getmenu():
    choice = menu.get()
    return(choice)

def closeprgm():
    Waistsrvo.stop()
    LowerArmsrvo.stop()
    UpperArmsrvo.stop()
    Wristsrvo.stop()
    Wristrtnsrvo.stop()
    GPIO.cleanup()
    Window.destroy()
    
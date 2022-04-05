from tkinter import *

from tkinter.ttk import *

from functions import *


#Button to close program
closebtn = Button(Window,text = "Close Program",command = Window.destroy)

#motor control buttons
btn = Button(Window, text = "click to rotate",command = motorselect)
btn.pack()
closeclaw = Button(Window, text = "Click to toggle claw")
closeclaw.pack()
closebtn.pack()





mainloop()
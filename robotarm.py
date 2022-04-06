from tkinter import *

from tkinter.ttk import *

from servologic import *

from functions import *


#Button to close program
closebtn = Button(Window,text = "Close Program",command=lambda: closeprgm())

#motor control buttons
btn = Button(Window, text = "click to rotate",command = motorselect)
btn.pack()
closeclaw = Button(Window, text = "Click to toggle claw")
closeclaw.pack()
closebtn.pack()






mainloop()
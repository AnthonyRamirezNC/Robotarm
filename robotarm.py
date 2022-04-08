from tkinter import *

from tkinter.ttk import *

from servologic import *

from functions import *


#Button to close program
closebtn = Button(Window,text = "Close Program",command=lambda: closeprgm()).pack()

#motor control buttons
btn = Button(Window, text = "click to rotate",command = motorselect).pack()
closeclaw = Button(Window, text = "Click to close claw",command=lambda: clsclaw()).pack()

openclaw = Button(Window,text = "Click To Open Claw",command=lambda: opnclaw()).pack()





mainloop()
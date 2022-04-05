from tkinter import *

from tkinter.ttk import *

from functions import *




#Button to close program
closebtn = Button(Window,text = 'Close Program',command = Window.destroy)

#button to show button
btn = Button(Window, text = "click to rotate",command = textbox)
btn.pack()
closeclaw = Button(Window, text = "Click to toggle claw")
closeclaw.pack()
closebtn.pack()



mainloop()
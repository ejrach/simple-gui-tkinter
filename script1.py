from tkinter import *


# Basic description of the GUI control layout.
# If this is the window, then controls are placed
# in this grid
#          column
#       =====================================
#  row  |     0,0   |    0,1    |    0,2    |
#       =====================================
#       |     1,0   |    1,1    |    1,2    |
#       =====================================



# create the active window
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

# create a button widget, and tell it "which container" to be displayed
# https://www.tutorialspoint.com/python/tk_button
b1 = Button(window, text = "Execute", command = km_to_miles)
# tell the button where to be displayed in the window
b1.grid(row=0,column=0)

# create an entry widget (takes user input)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# create a text widget
t1 = Text(window, height=1,width=20)
t1.grid(row=0,column=2)


# 
window.mainloop()


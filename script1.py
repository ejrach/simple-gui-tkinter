from tkinter import *

# Basic description of the GUI control layout.
# If this is the window, then controls are placed
# in this grid based off a row,column coordinate system.
#
#          column
#       =====================================
#  row  |     0,0   |    0,1    |    0,2    |
#       =====================================
#       |     1,0   |    1,1    |    1,2    |
#       =====================================

# create the active window
window = Tk()

def kg_conversion():
    grams = float(kg_e_value.get())*1000
    pounds = float(kg_e_value.get())*2.20462
    ounces = float(kg_e_value.get())*35.274
    tbGrams.insert(END,grams)
    tbPounds.insert(END, pounds)
    tbOunces.insert(END, ounces)

# create a label widget, and tell it "which container" to be displayed
lblKg = Label(window, text="Kg")
lblKg.grid(row=0, column=0)

# entry widget for kg (takes user input), placed in the window container
kg_e_value = StringVar()
e1 = Entry(window, textvariable=kg_e_value)
e1.grid(row=0, column=1)

# create a button widget, and tell it "which container" to be displayed
# https://www.tutorialspoint.com/python/tk_button
btnConvert = Button(window, text = "Convert", command = kg_conversion)
# tell the button where to be displayed in the window
btnConvert.grid(row=0,column=2)

# text widget for grams display, placed in the window container
tbGrams = Text(window, height=1,width=10)
tbGrams.grid(row=1,column=0)

# text widget for pounds display, placed in the window container
tbPounds = Text(window, height=1,width=10)
tbPounds.grid(row=1,column=1)

# text widget for ounces display, placed in the window container
tbOunces = Text(window, height=1,width=10)
tbOunces.grid(row=1,column=2)

# Execute the main loop of tkinter
window.mainloop()


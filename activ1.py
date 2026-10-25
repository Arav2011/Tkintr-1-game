# Import necessary libariries
from tkinter import *
from datetime import date
# create window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x400')

# add widgets
# add label
lbl = Label(text="Hey There!" ,fg="white", bg="#622CE9", height=1, width=300)

# add label for getting name as input from user
# use entry widget to creat a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#2D544D")
name_entry = Entry()

#function to display
def display():
    # read input given by user
    name = name_entry.get()
    #Declaring a global variable
    # to make it accessible anywhere in the program
    global Message
    message = "Welcome to the Application! \nTodays date is : "
    greet = "Hello "+name+"\n"
    # display details in a text box
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# Add a text Widget to display information/messages
text_box = Text(height=3)

# Add button and give it a commaand as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')
    
# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# start the main loop 
root.mainloop()
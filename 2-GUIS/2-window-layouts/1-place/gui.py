from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

    # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                   height=300, 
                   width=400)
                   
        self.add_heading_label()
        self.add_middle_label()
        self.add_button()
        self.add_entry()
        #self.add_border()


    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)
    
    # style
        self.heading_label.configure(font="Arial 24",text="Receive our newsletter")

    def add_middle_label(self):
        self.middle_label = Label()
        self.middle_label.place(x=0, y=100)
        self.middle_label.configure(font="Arial 10", text="Please enter your email below to receive our newsletter")

    def add_button(self):
        self.button = Button()
        self.button.place(x=100, y=200)
        self.button.configure(font="comic 12", text="Subscribe")

    def add_entry(self):
        self.entry = Entry()
        self.entry.place(x=100, y=150)
        self.entry.configure(font="comic 12", text="Enter your mail here")

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


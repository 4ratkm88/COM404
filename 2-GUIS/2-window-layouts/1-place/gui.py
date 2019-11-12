from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

    # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                   height=500, 
                   width=500)
                   
        self.add_heading_label()


    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)
    
    # style
        self.heading_label.configure(font="Arial 24",
                                 text="Receive our newsletter")

    def add_middle_label(self):
        self.middle_label = Label()
        self.middle_label.place(x=100, y=100)
        self.middle_label.configure(font="Arial 12", text="Middle Label")

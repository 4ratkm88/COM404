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
        #self.add_email_frame()
        #self.add_border()

   
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.grid(row=1, column=3, columnspan=1)

    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.grid(row=2, column=3, columnspan=5)
        self.heading_label.configure(font="Arial 24",text="Receive our newsletter")

    
    # style
    def add_middle_label(self):
        self.middle_label = Label()
        self.middle_label.grid(row=3, column=3, columnspan=5)
        self.middle_label.configure(font="Arial 10", text="Please enter your email below to receive our newsletter")

    def add_entry(self):
        self.entry = Entry()
        self.entry.grid(row=5, column=3, columnspan=5)
        self.entry.configure(font="comic 12", text="Enter your mail here")

    def add_button(self):
        self.button = Button()
        self.button.grid(row=7, column=3, columnspan=5)
        self.button.configure(font="comic 12", text="Subscribe")

    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


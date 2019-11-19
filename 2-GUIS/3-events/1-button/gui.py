from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

    # set window attributes
        self.title("Tickety Boo")
        
        self.configure(bg="#eee",
                   height=300, 
                   width=400)          
        self.add_heading_label()
        self.add_instruction_label()
        self.add_tickets_entry()
        self.add_buy_button()
        #self.add_email_frame()
        #self.add_border()

   
    def add_email_frame(self):
        pass

    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        pass

    
    # style
    def instruction_label(self):
        pass

    def add_tickets_entry(self):
        pass

    def add_buy_button(self):
        pass

    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


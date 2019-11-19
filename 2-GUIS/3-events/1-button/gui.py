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
        self.heading_label.grid(row=1, column=3, columnspan=1)
        self.heading_label.configure(font="Arial 24",text="Entrance ticket")

    
    # style
    def add_instruction_label(self):
        self.add_instruction_label = Label()
        self.add_instruction_label.grid(row= 2, column=3, columnspan=1)
        self.add_instruction_label.configure(font="Arial 20", text="How many tickets to buy?")

    def add_tickets_entry(self):
        self.add_tickets_entry_label = Entry()
        self.add_tickets_entry.grid(row=3, column=1, columnspan=3)
        pass

    def add_buy_button(self):
        self.add_buy_button = Button()
        self.add_buy_button.grid(row=4,column=4,columnspan=5)
        self.add_buy_button.config(font="Arial 15", Text="buy")

    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


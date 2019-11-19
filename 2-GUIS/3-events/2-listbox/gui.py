from tkinter import *
from tkinter import messagebox

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
        self.heading_label.grid(row=1, column=1, columnspan=1)
        self.heading_label.configure(font="Arial 24",text="Entrance ticket")

    
    # style
    def add_instruction_label(self):
        self.add_instruction_label = Label()
        self.add_instruction_label.grid(row=2, column=1, columnspan=1)
        self.add_instruction_label.configure(font="Arial 20", text="How many tickets to buy?")

    def add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=3, column=1, columnspan=1)
        self.tickets_entry.configure(font="Arial 10", text="Text")

    def add_buy_button(self):
        self.add_buy_button = Button()
        self.add_buy_button.grid(row=4,column=1,columnspan=1)
        self.add_buy_button.configure(font="Arial 15", text="buy")
    #events
        self.add_buy_button.bind("<ButtonRelease-1>", self.buy_button_clicked)
        
    def buy_button_clicked(self, event):
        Numtic = self.tickets_entry.get()
        messagebox.showinfo("Purchased!", "You have purchased "+ Numtic +" tickets!")
    

    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


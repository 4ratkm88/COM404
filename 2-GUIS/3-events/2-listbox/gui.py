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
        self.add_instruction_label2()
        self.add_lyricadd_entry()
        self.add_lyricadd_button()
        self.add_lyric_listbox()
        #self.add_email_frame()
        #self.add_border()

    def add_heading_label(self):
    # create   
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0, columnspan=2)
        self.heading_label.configure(font="Arial 24",text="Song Maker")

    
    # style
    def add_instruction_label(self):
        self.add_instruction_label = Label()
        self.add_instruction_label.grid(row=2, column=0, columnspan=2)
        self.add_instruction_label.configure(font="Arial 20", text="Lyric to add")

    def add_instruction_label2(self):
        self.add_instruction_label2 = Label()
        self.add_instruction_label2.grid(row=4, column=1, columnspan=1)
        self.add_instruction_label2.configure(font="Arial 20", text="Lyrics")
   
    def add_lyricadd_entry(self):
        self.lyricadd_entry = Entry()
        self.lyricadd_entry.grid(row=3, column=1, columnspan=3)
        self.lyricadd_entry.configure(font="Arial 10", text="Text")

    def add_lyricadd_button(self):
        self.lyricadd_button = Button()
        self.lyricadd_button.grid(row=3,column=3,columnspan=3)
        self.lyricadd_button.configure(font="Arial 15", text="Add")
    #events
        self.lyricadd_button.bind("<ButtonRelease-1>", self.lyricadd_button_clicked)
        
    def lyricadd_button_clicked(self, event):
        Numtic = self.lyricadd_entry.get()
        messagebox.showinfo("Purchased!", "You have purchased "+ Numtic +" tickets!")
    
    def add_lyric_listbox(self):
        self.lyric_listbox = Listbox()
        self.lyric_listbox.grid(row=5, column=2, columnspan=3)
        

    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()


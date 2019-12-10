from tkinter import *
from tkinter import messagebox

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()
    #Load picture
        self.santa_image = PhotoImage(file="U:\\python\\COM404\\TCA2\\part_A\\santa.gif")
    # set window attributes
        self.title("Letter to Santa")
        self.configure(bg="#f66",
                   height=300, 
                   width=400)          
        self.add_heading_label()
        self.add_global_frame()
        self.add_name_label()
        self.add_name_entry()
        self.add_santa_image_label
        #self.add_email_frame()
        #self.add_border()

    def add_heading_label(self):
    # create   
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=1, column=0, columnspan=2)
        self.heading_label.configure(pady="40", font="Arial 18", fg="#fff", bg="#f33",text="Write to Santa!")

    def add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=1, column=0)
        self.global_frame.configure(bg="#f33",width=1920, height=1080)
    # style
    def add_name_label(self):
        self.name_label = Label(self.global_frame)
        self.name_label.grid(row=2, column=0, columnspan=2)
        self.name_label.configure(font="Arial 12", fg="#fff", bg="#f33",text="Your Name")

    def add_name_entry(self):
        self.name_entry = Label()
        self.name_entry.grid(row=4, column=1, columnspan=1)
        self.name_entry.configure(font="Arial 20", text="")
   
    def add_santa_image_label(self):
        self.santa_image_label = Label()
        self.santa_image_label.grid(row=1, column=1)
        self.santa_image_label.configure(image=self.santa_image)

    def add_post_button(self):
        self.post_button = Button()
        self.post_button.grid(row=3,column=3,columnspan=3)
        self.post_button.configure(bg="#ff0", font="Arial 15", text="Post Letter")
    #events
        self.post_button.bind("<ButtonRelease-1>", self.post_button_clicked)
    
    def post_button_clicked(self, event):
        messagebox.showinfo("Posted :)") 

    def add_letter_text(self):
        self.letter_text = Entry()
        self.letter_text.grid(row=3, column=1, columnspan=3)
        self.letter_text.configure(font="Arial 10", text="Text")

        
        
    

    #def add_border(self):
        #self.border = Bd()
        #self.border.place(x=280, y=380)
        #self.border.configure()
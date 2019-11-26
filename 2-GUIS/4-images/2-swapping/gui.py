from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cacti_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\2-swapping\\cacti.gif")
        self.cacti_noname_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\2-swapping\\cacti2.gif")
        self.cacti_name_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\2-swapping\\cacti3.gif")
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_cacti_image_label()
        self.add_cacti_button()
        
  

    def add_heading_label(self):  
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=1, columnspan=3, sticky=W+E+N+S)
        self.heading_label.configure(font="Arial 19",text="Cactus Leaves") 

    def add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column=1)
        self.cacti_image_label.configure(image=self.cacti_image,height=400,width=600)
        

    def add_cacti_button(self):
        self.add_cacti_button = Button()
        self.add_cacti_button.grid(row=3,column=1,columnspan=1)
        self.add_cacti_button.configure(font="Arial 15", text="Flip")  
        self.add_cacti_button.bind("<ButtonRelease-1>", self.cactinoname_clicked) 
        self.add_cacti_button.bind("<ButtonRelease-3>", self.cacti_name_clicked) 

    def cactinoname_clicked(self, event):
        #Numtic = self.tickets_entry.get()
        #messagebox.showinfo("Purchased!", "You have purchased "+ Numtic +" tickets!")                                   
        self.cacti_image_label.configure(image = self.cacti_noname_image)
    
    def cacti_name_clicked(self,event):
        self.cacti_image_label.configure(image = self.cacti_name_image)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
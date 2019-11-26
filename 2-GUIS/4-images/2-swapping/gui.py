from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\2-swapping\\cacti.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_ambulance_image_label()
  

    def add_heading_label(self):  
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=1, columnspan=3, sticky=W+E+N+S)
        self.heading_label.configure(font="Arial 19",text="Transport") 

    def add_cacti_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column=1)
        self.cacti_image_label.configure(image=self.cacti_image,
                                             height=600,
                                             width=600)

    
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
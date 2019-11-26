from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:/python/COM404/2-GUIS/4-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/python/COM404/2-GUIS/4-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="U:/python/COM404/2-GUIS/4-images/1-loading/plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()
        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=0, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def add_bike_image_label():
        pass
 
    def add_plane_image_label():
        pass
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
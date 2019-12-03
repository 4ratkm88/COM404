from tkinter import *
from tkinter import messagebox
class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\3-positioning\\map.gif")
        self.bus_image = PhotoImage(file="U:\\python\\COM404\\2-GUIS\\4-images\\3-positioning\\bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_bus_image_label()
        self.add_map_frame()
        self.add_heading_label()
        self.add_map_image_label()
        self.bus_move()

        self.map_frame = Frame()
        self.map_frame.configure(width=400, height=400)

        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)

        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=bus_image)
    
   
   
   

    def bus_move(self, event):
        messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
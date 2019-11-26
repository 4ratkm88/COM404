from tkinter import *

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

    def add_heading_label(self):  
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=3, sticky=W+E+N+S)
        self.heading_label.configure(font="Arial 19",text="Bus Journey") 
    
    def add_map_frame():
        self.map_frame = Frame()
        self.map_frame.configure(width=400, height=400)
   
    
   

    def bus_move(self, event):
        messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
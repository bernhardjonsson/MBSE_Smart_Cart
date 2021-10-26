import tkinter as tk
import tkinter.scrolledtext as st
import time
from tkinter import *


class GUI_sim(tk.Tk):
    def __init__(self):
        super().__init__()
        # setup up root frame
        self.title('Supermarket')
        self.geometry('900x800')

        # setup supermarket frame
        self.SupM_frame = Frame(self)
        self.SupM_frame.pack(side = LEFT)
        self.canvas = Canvas(self.SupM_frame, width = 620, height = 800, bg = self._color((230,230,230)))
        self._SuperMarket_setup()
        self.canvas.pack()

        # setup info frame
        self.info_frame = Frame(self)
        self.info_frame.pack(side = RIGHT)
        tk.Label(self.info_frame,
                text = "Simulation info", 
                font = ("Times New Roman", 15), 
                foreground = "black").grid(column = 0,
                row = 0)

        # Create scrolled text area as Read Only
        self.text_area = st.ScrolledText(self.info_frame,
                width = 20, 
                height = 30, 
                font = ("Times New Roman",
                    15))
        
        self.text_area.grid(column = 0, pady = 10, padx = 10)
        self.text_area.configure(state = 'disable')

    def _SuperMarket_setup(self):
        #window shelvs
        self.canvas.create_rectangle(0,0,40,600,width = 2, fill = self._color((140,140,140)))
        self.canvas.create_rectangle(0,0,400,40,width = 2, fill = self._color((140,140,140)))
        self.canvas.create_rectangle(480,0,620,40,width = 2, fill = self._color((140,140,140)))
        self.canvas.create_rectangle(580,0,620,700,width = 2, fill = self._color((140,140,140)))

        #create inner shelves
        x0 = 120
        while x0 < 600:
            self.canvas.create_rectangle(x0,120,x0+40,300,width = 2, fill = self._color((140,140,140)))   
            self.canvas.create_rectangle(x0,380,x0+40,600,width = 2, fill = self._color((140,140,140)))
            x0 = x0 + 120

    def _color(self,rgb):
        return "#%02x%02x%02x" % rgb 


    def add_msg(self, msg):
        print(msg)
        print(tk.INSERT)
        self.text_area.insert("end",msg)




#root = Tk()
#root.title('Supermarket')

#canvas = Canvas(root, width = 600, height = 800, bg = "#%02x%02x%02x" % (230,230,230))
#canvas.pack()

#for i in range(40) : # Vertical Lines
#    x = 40 + (i * 40)
#    canvas.create_line(x,800,x,-800,width = 2)


#for i in range(40) : # Horizontal Line
#    y = 40 - (i * 40)
#    canvas.create_line(600,-y,10,-y,width = 2)


#canvas.create_rectangle(0,0,40,600,width = 2, fill = "#%02x%02x%02x" % (140,140,140))
#canvas.create_rectangle(0,0,600,40,width = 2, fill = "#%02x%02x%02x" % (140,140,140))

#root.mainloop()

if __name__ == "__main__":
    gui = GUI_sim()
    gui.mainloop()
    my_msg = "Hello World "
    for i in range(100):
        gui.add_msg(my_msg + str(i))
        time.sleep(2)



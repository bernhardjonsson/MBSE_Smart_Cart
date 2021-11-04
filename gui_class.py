import tkinter as tk
import tkinter.scrolledtext as st
import time
from tkinter import *


class GUI_sim(tk.Tk):
    def __init__(self, store_setup=""):
        super().__init__()
        # setup up root frame
        self.title('Supermarket')
        self.geometry('900x800')

        # setup supermarket frame
        self.SupM_frame = Frame(self)
        self.SupM_frame.pack(side = LEFT)
        self.SupM_frame.canvas = Canvas(self.SupM_frame, width = 620, height = 800, bg = self._color((230,230,230)))
        self._SuperMarket_setup(store_setup)
        self.SupM_frame.canvas.pack()

        """
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
        """

    def _SuperMarket_setup(self,setup_file):
        if setup_file is not  "":
            self._SuperMarket_from_file(setup_file)
        else:
            #Set up standard store
            #window shelvs
            self.SupM_frame.canvas.create_rectangle(0,0,40,600,width = 2, fill = self._color((140,140,140)))
            self.SupM_frame.canvas.create_rectangle(0,0,400,40,width = 2, fill = self._color((140,140,140)))
            self.SupM_frame.canvas.create_rectangle(480,0,620,40,width = 2, fill = self._color((140,140,140)))
            self.SupM_frame.canvas.create_rectangle(580,0,620,700,width = 2, fill = self._color((140,140,140)))

            #create inner shelves
            x0 = 120
            while x0 < 600:
                self.SupM_frame.canvas.create_rectangle(x0,120,x0+40,300,width = 2, fill = self._color((140,140,140)))   
                self.SupM_frame.canvas.create_rectangle(x0,380,x0+40,600,width = 2, fill = self._color((140,140,140)))
                x0 = x0 + 120

    def _SuperMarket_from_file(self,setup_file):
        f = open(setup_file)
        lines = f.readlines()
        print(lines)

    def _color(self,rgb):
        return "#%02x%02x%02x" % rgb 


    def add_msg(self, msg):
        #DOESN'T work
        print(msg)
        print(tk.INSERT)
        self.text_area.insert("end",msg)


    def place_customer(self,pos,cust_id):
        self.SupM_frame.canvas.create_oval(pos[0]-5, pos[1]-5, pos[0]+5, pos[1]+5, fill = cust_id, width = 2)
        self._draw_cross(pos[0]-10,pos[1]-10,cust_id)

    def _draw_cross(self,x,y,cust_id):
        self.SupM_frame.canvas.create_line(x,y,x+5,y+5, fill = cust_id, width = 2)
        self.SupM_frame.canvas.create_line(x,y,x-5,y-5, fill = cust_id, width = 2)
        self.SupM_frame.canvas.create_line(x,y,x+5,y-5, fill = cust_id, width = 2)
        self.SupM_frame.canvas.create_line(x,y,x-5,y+5, fill = cust_id, width = 2)
        



if __name__ == "__main__":
    gui = GUI_sim()

    PATH_1 = [(20,650),(80,650)]
    
    
    gui.place_customer(PATH_1[0],"red")
    
    #for i in range(1,100):
        




     #   time.sleep(1)
    
    gui.mainloop()

    #my_msg = "Hello World "
    #for i in range(100):
    #    gui.add_msg(my_msg + str(i))
    #    time.sleep(2)



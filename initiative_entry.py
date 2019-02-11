from tkinter import *

class Initiative_entry:
    def __init__(self, initiative, name, is_player, frame):
        self.initiative = initiative
        self.name = name
        self.is_player = is_player
        self.frame = frame
        self.deleted = False
        
    def __eq__(self, other):
        return self.initiative == other.initiative
    
    def __lt__(self, other):
        return self.initiative < other.initiative
    
    def delete_grid(self):
        self.ini.grid_forget()
        self.nam.grid_forget()
        self.rem.grid_forget()
        self.deleted = True
    
    def create_grid(self, i):
        self.ini = Label(self.frame,text=self.initiative,width=2)
        self.ini.grid(column=0, row=i)
        self.nam = Label(self.frame, text=self.name)
        self.nam.grid(column=1, row=i)
        self.rem = Button(self.frame, text='-', command=self.delete_grid)
        self.rem.grid(column=2, row=i)
    
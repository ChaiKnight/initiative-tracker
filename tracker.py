# !/usr/bin/python3
import tkinter as tk
from tkinter import *
from initiative_entry import Initiative_entry

initiative_list = []

top = tk.Tk()

frame = Frame(top)
frame.pack(side=BOTTOM)

def update_grid():
    global initiative_list

    for label in frame.grid_slaves():
        label.grid_forget()
    
    for i in reversed(range(len(initiative_list))):
        entry = list(reversed(sorted(initiative_list)))[i]
        if entry.deleted:
            initiative_list.pop(i)
            continue
        entry.create_grid(i)
        print(i)
        

bottomframe = Frame(top)
bottomframe.pack(side=BOTTOM)

i = Entry(top, bg="white", width=3)
i.pack(side=LEFT)

e = Entry(top, bg="white")
e.pack(side=LEFT)

playerVar = IntVar()
player_checkbox = tk.Checkbutton(top, text="Player?", variable=playerVar,
                                 onvalue=1, offvalue=0)
player_checkbox.pack(side=RIGHT)

def add_new_entry():
    try:
        initiative = int(i.get())
        name = e.get()
        is_player = int(playerVar.get()) == 1
        
        if len(name)==0:
            messagebox.showwarning("Warning", 
                                   "Name must be longer than 0 characters")
            return
        
        new_entry = Initiative_entry(initiative, name, is_player, frame)
        initiative_list.append(new_entry)
        
        update_grid()
    except ValueError:
        messagebox.showwarning("Warning", "First box must contain an integer")
    


add_button = tk.Button(top, text="+", command=add_new_entry)
add_button.pack(side=RIGHT)


def cb_clearNPC():
    global initiative_list
    for i in reversed(range(len(initiative_list))):
        print(initiative_list[i].is_player)
        if not initiative_list[i].is_player:
            initiative_list[i].delete_grid()
            initiative_list.pop(i)
    update_grid()
    
    
def cb_clear_all():
    global initiative_list
    for entry in initiative_list:
        entry.delete_grid()
    initiative_list.clear()
    update_grid()


clearNPC_button = tk.Button(bottomframe, text="Clear NPCs", command=cb_clearNPC)
clearNPC_button.pack(side=LEFT)

clear_all_button = tk.Button(bottomframe, text="Clear All", 
                             command=cb_clear_all)
clear_all_button.pack(side=RIGHT)


top.mainloop()
import os
import shutil
from tkinter import *
import tkinter as tk

def sort():
    directory = entry_1.get()
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            x = directory+"/"+filename
            y = directory+"/Video"
            try:
                os.mkdir(y)
            except FileExistsError:
                y = y
            shutil.move(x, y)
        elif filename.endswith(".mp3"):
            x = directory+"/"+filename
            y = directory+"/Music"
            try:
                os.mkdir(y)
            except FileExistsError:
                y = y
            shutil.move(x, y)
        elif filename.endswith(".pdf"):
            x = directory+"/"+filename
            y = directory+"/Documents"
            try:
                os.mkdir(y)
            except FileExistsError:
                y = y
            shutil.move(x, y)
        else:
            pass
    exit()

#######################################   GUI    ############################

root = tk.Tk()
root.title("Sorting")

label_1 = Label(root, text="Please Enter the Directory:")
entry_1 = Entry(root)
button_1 = Button(root, text="Click to sort files", command=sort)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=2)
button_1.grid(row=1, column=1)

root.mainloop()
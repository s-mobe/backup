# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:34:51 2021

@author: Omar
"""

import tkinter
from tkinter import filedialog
from tkinter import ttk
import file_length as fl
import file_dir_cmp as flc


def selectpath():
    """
    tkinter function to select the path to run os.walk

    """
    filepath = tkinter.filedialog.askdirectory(parent= file_length)
    entry1.delete(0, "end")
    entry1.insert("end",filepath)
    
def savefile():
    """
    the path to save the return txt file

    """
    filepath = tkinter.filedialog.askdirectory(parent= file_length)
    entry3.delete(0, "end")
    entry3.insert("end",filepath)
    
def runcommand():
    """
    gets the entry values to run the function check file

    """
    fl.checkfile(entry1.get(), entry2.get(),entry3.get())

def selectpath_source():
    filepath = tkinter.filedialog.askdirectory(parent= backup)
    entry1b.delete(0, "end")
    entry1b.insert("end",filepath)

def selectpath_destination():
    filepath = tkinter.filedialog.askdirectory(parent= backup)
    entry2b.delete(0, "end")
    entry2b.insert("end",filepath)
    
def start_backup():
    flc.make_ob(entry1b.get(), entry2b.get())

window = tkinter.Tk()
window.geometry("350x200")
window.wm_title("File Length")
window.resizable(width=False, height=False)

tabcontrol = ttk.Notebook(window)
tabcontrol.grid(row=0,column=0)

file_length = ttk.Frame(tabcontrol)
backup = ttk.Frame(tabcontrol)

file_length.grid(row=0, column=1)
backup.grid(row=0, column=0)

tabcontrol.add(file_length, text="File Length")
tabcontrol.add(backup, text="Backup")

p = ttk.Progressbar(window,orient="horizontal", length=200,mode="indeterminate")
p.grid(row=8, column=0)

#-------------Labels entries and buttons----------------
#-------------- File length-------------------------------
label1 = tkinter.Label(file_length,text="Folder path" )
label1.grid(row=1, column=0)

label2 = tkinter.Label(file_length, text="File/Folder name length")
label2.grid(row=2, column=0)

label3 = tkinter.Label(file_length, text="Path to save")
label3.grid(row=4, column=0)

entry1 = tkinter.Entry(file_length)
entry1.grid(row=1, column=1)

entry2string = tkinter.StringVar(value = 225)
entry2 = tkinter.Entry(file_length, textvariable = entry2string)
entry2.grid(row=2, column=1)

entry3 = tkinter.Entry(file_length)
entry3.grid(row=4, column=1)

button1 = tkinter.Button(file_length, text="Browse", command=selectpath)
button1.grid(row=1, column=3)

button2 = tkinter.Button(file_length, text="browse", command=savefile )
button2.grid(row=4, column=3)

#------------------padding--------------------#
label10 = tkinter.Label(file_length,text="   ")
label10.grid(row=3,column=2)


label11 = tkinter.Label(file_length, text ="  ")
label11.grid(row=5,column=0)

#-----------------execute buttong-----------------

buttonexe = tkinter.Button(file_length, text="  OK  ", command=runcommand)
buttonexe.grid(row=6, column=0)

#------------------- File length end --------------------------------
#------------------- backup app start -------------------------------

label1b = tkinter.Label(backup,text="Source Path" )
label1b.grid(row=1, column=0)

label1b = tkinter.Label(backup,text="   ")
label1b.grid(row=2,column=2)

label2b = tkinter.Label(backup, text="Destination path")
label2b.grid(row=3, column=0)

entry1b = tkinter.Entry(backup)
entry1b.grid(row=1, column=1)

entry2b = tkinter.Entry(backup)
entry2b.grid(row=3, column=1)

button1b = tkinter.Button(backup, text="Browse", command=selectpath_source)
button1b.grid(row=1, column=2)

button2b = tkinter.Button(backup, text="browse", command=selectpath_destination )
button2b.grid(row=3, column=2)

label2b = tkinter.Label(backup,text="   ")
label2b.grid(row=4,column=2)

buttonexe_b = tkinter.Button(backup, text="  Backup  ", command=start_backup)
buttonexe_b.grid(row=5, column=1)

window.mainloop()
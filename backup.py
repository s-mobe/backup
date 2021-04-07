# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:34:51 2021

@author: Omar
"""

import tkinter
import os
import sys
import filecmp
import shutil
import win32api
from tkinter import filedialog, ttk
import threading


def loading(func):
    """
    Parameters
    ----------
    wrapper function to start the progress bar
        
    Returns
    -------
    wrapper : TYPE : function

    """
    def wrapper(*args, **kwargs):
        p.start(5)
        func(*args, **kwargs)
        p.stop()
    return wrapper

@loading
def checkfile(path, thelength, savepath):
    """
    
    Parameters
    ----------
    path : TYPE : string
        DESCRIPTION : the path of the folder to walk
    thelength : TYPE : int
        DESCRIPTION: the length of the file or folder path to be checked
    savepath : TYPE : string
        DESCRIPTION : path to the folder to save the report as report.txt

    Returns
    -------
    txt file with all the path and file name => the length 

    """
    thedict={}
    thelength = int(thelength)
    for a, b, c in os.walk(path):
        for file in c:
           # print("file length" + str(len(file) + len(a)))
            if len(file) + len(a) > thelength:
                if a in thedict:
                    thedict[a].append(file)
                else:
                    thedict[a] = []
                    thedict[a].append(file)
        for dirct in b:
            #print(len(dirct) + len(a))
            if len(dirct) + len(a) > thelength:
                if a in thedict:
                    thedict[a].append(dirct)
                else:
                    thedict[a] = []
                    thedict[a].append(dirct)
        
    
                
    with open(savepath +"/report.txt", "w") as txt:
        for k in thedict:
            for i in range(len(thedict[k])):
                txt.write("{} : {} \n\n".format(k,thedict[k][i]))
    return txt

def make_ob(source,dest):
    """
    Parameters
    ----------
    source : TYPE : string
        DESCRIPTION: path of the source folder
    dest : TYPE : string
        DESCRIPTION: path to the destination folder

    Returns
    -------
    TYPE : filecmp object from source and destination
        DESCRIPTION: creates filecmp.dircmp object to the backup function

    """
    return back_up(filecmp.dircmp(source, dest))

@loading
def back_up(dircmpp):
    
    for name in dircmpp.diff_files:       
        try:

            print("copying {} from {} to {} ".format(name, dircmpp.left, dircmpp.right))
            shutil.copyfile(dircmpp.left + "/{}".format(name), dircmpp.right + "/{}".format(name))
        
        except:
            
            print(" trying copying {} from {} to {} ".format(name, dircmpp.left, dircmpp.right))
            pathleft = win32api.GetShortPathName(dircmpp.left)
            pathright = win32api.GetShortPathName(dircmpp.right)
            shutil.copyfile(pathleft + "/{}".format(name), pathright + "/{}".format(name))
                              
    for name in dircmpp.left_only:
        
        if os.path.isdir(dircmpp.left+"/{}".format(name)):
            
            print("copying tree" , "{}{} \n".format(dircmpp.right,name))
            shutil.copytree("{}/{}".format(dircmpp.left, name), "{}/{}".format(dircmpp.right,name))
        else:           
            try:                
                shutil.copyfile(dircmpp.left+"/{}".format(name), dircmpp.right+"/{}".format(name))           
            except Exception as e :
                
                print(e)
                print("failed copying {} IN {}".format(name,dircmpp.left))
                continue
                
    for name in dircmpp.subdirs.values():
        #print(name.left, " -- " , name.right)
        newdir = filecmp.dircmp(name.left,name.right)
        back_up(newdir)
    
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
    gets the entry values to run the function checkfile on a 
    seperate thread

    """   
    thetask = threading.Thread(target=checkfile,args=(entry1.get(), entry2.get(),entry3.get()))
    thetask.start()

def selectpath_source():
    """
    Returns
    -------
    select the path of the source directory and put it in the entry

    """
    filepath = tkinter.filedialog.askdirectory(parent= backup)
    entry1b.delete(0, "end")
    entry1b.insert("end",filepath)

def selectpath_destination():
    """
    Returns
    -------
    select the path of the destination directory and put it in the entry

    """
    filepath = tkinter.filedialog.askdirectory(parent= backup)
    entry2b.delete(0, "end")
    entry2b.insert("end",filepath)
    
def start_backup():
    """
    Returns
    -------
    calls the make_ob function with a seperate thread

    """
    the_backup= threading.Thread(target=make_ob, args=(entry1b.get(), entry2b.get()))
    the_backup.start()
    
#---------------start of gui -------------------------------   

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

#---------------------- padding --------------------------------

label2b = tkinter.Label(backup,text="   ")
label2b.grid(row=4,column=2)

#------------------------ execute button for the back up ---------

buttonexe_b = tkinter.Button(backup, text="  Backup  ", command=start_backup)
buttonexe_b.grid(row=5, column=1)

window.mainloop()
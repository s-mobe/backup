# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os 
# import tkinter
# from tkinter import filedialog


# def selectpath():
#     """
#     tkinter function to select the path to run os.walk

#     """
#     filepath = tkinter.filedialog.askdirectory(parent=window)
#     entry1.delete(0, "end")
#     entry1.insert("end",filepath)
    
# def savefile():
#     """
#     the path to save the return txt file

#     """
#     filepath = tkinter.filedialog.askdirectory(parent=window)
#     entry3.delete(0, "end")
#     entry3.insert("end",filepath)
    
# def runcommand():
#     """
#     gets the entry values to run the function check file

#     """
#     checkfile(entry1.get(), entry2.get(),entry3.get())

def checkfile(path, thelength, savepath):
    """
    
    Parameters
    ----------
    path : TYPE : string
        DESCRIPTION : the path of the folder to walk
    thelength : TYPE : int
        DESCRIPTION: the length of the file or folder to be checked
    savepath : TYPE : string
        DESCRIPTION : path to the folder to save the report

    Returns
    -------
    txt file with all the path and file name matching the length 

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
                
# window = tkinter.Tk()

# window.geometry("350x150")
# window.wm_title("File Length")
# window.resizable(width=False, height=False)

# #-------------Labels entries and buttons----------------
# label1 = tkinter.Label(window,text="Folder path" )
# label1.grid(row=0, column=0)

# label2 = tkinter.Label(window, text="File/Folder name length")
# label2.grid(row=1, column=0)

# label3 = tkinter.Label(window, text="Path to save")
# label3.grid(row=3, column=0)

# entry1 = tkinter.Entry(window)
# entry1.grid(row=0, column=1)

# entry2string = tkinter.StringVar(value = 225)
# entry2 = tkinter.Entry(window, textvariable = entry2string)
# entry2.grid(row=1, column=1)

# entry3 = tkinter.Entry(window)
# entry3.grid(row=3, column=1)

# button1 = tkinter.Button(window, text="Browse", command=selectpath)
# button1.grid(row=0, column=3)

# button2 = tkinter.Button(window, text="browse", command=savefile )
# button2.grid(row=3, column=3)

# #------------------padding--------------------#
# label10 = tkinter.Label(window,text="   ")
# label10.grid(row=2,column=2)


# label11 = tkinter.Label(window, text ="  ")
# label11.grid(row=4,column=0)

# #-----------------execute buttong-----------------

# buttonexe = tkinter.Button(window, text="  OK  ", command=runcommand)
# buttonexe.grid(row=5, column=0)


# window.mainloop()
    
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 00:30:31 2021

@author: Omar
"""

import os
import sys
import filecmp
import shutil
import win32api


# source = "C:/Users/Omar/Documents/Welo - copy/"
# dest = "C:/Users/Omar/Documents/Welo/"

def make_ob(source,dest):
    return back_up(filecmp.dircmp(source, dest))

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
        
            
# thedir = filecmp.dircmp(source, dest)
# back_up(thedir)
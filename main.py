import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


#Controls
self.__thisTextArea.grid(sticky = N + E + S + W)

#Open a new file
self.__thisFileMenu.add_command(label = "New", command = self.__newFile)

#Open existing file
self.__thisFileMenu.add_command(label = "Open", command = self.__openFile)

#Save current File
self.__thisFileMenu.add_command(label = "Save", command = self.__saveFile)

#Create a line in the dialog
self.__thisFileMenu.add_separator()

#Terminate
self.__thisFileMenu.add_command(label = "Exit", command = self.__quitApplication)

#Menu
self.__thisMenuBar.add_cascade(label= "File", menu = self.__thisFileMenu)


#Cut feature 
self.__thisEditMenu.add_command(label = "Cut", command = self.__cut)

#Copy feature
self.__thisEditMenu.add_command(label = "Copy", command = self.__copy)

#Paste feature
self.__thisEditMenu.add_command(label = "Past", command = self.__paste)

#Menu
self.__thisMenuBar.add_cascade(label= "Edit", menu = self.__thisEditMenu)

#Description of the notepad
self.__thisHelpMenu.add_command(label = "About Notepad", command = self.__showAbout)

#Menu
self.__thisMenuBar.add_cascade(label= "Help", menu = self.__thisHelpMenu)

#Adding the Menu Bar
self.__root.config(menu = self.__thisMenuBar)

#Scroll bar will adjust automatically according to the content
self.__thisScrollBar.pack(side = RIGHT, fill = Y)




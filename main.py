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
self.__thisScrollBar.config(command = self.__thisTextArea.yview)
self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)


#Exit Function
def __quitApplication(self):
	self.__root.destroy()

def __showAbout(self):
	showinfo("Notepad", "Mrinal Verma")

def __openFile(self):
	self.__file = askopenfilename(defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text Document", ".txt")])
	
	#No file to open
	if self.__file == "":
		self.__file =None
	else:
		#Try to open the file and set the window title
		self.__root.title(os.path.basename(self.__file) + " - Notepad")
		self.__thisTextArea.delete(1.0, END)
		file = open(self.__file, "r")
		self.__thisTextArea.insert (1.0, file.read())
		file.close()

def __newFile(self):
	self.__root.title("Untitled - Notepad")
	self.__file = None
	self.__thisTextArea.delete(1.0, END)

def __saveFile(self):
	if self.__file == None
	self.__file = asksavesfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text Document", ".txt")])
		if self.__file == "":
			self.__file = None
		else:
			#Try to save the file
			file = open(self.__file, "w")
			file.write(self.__thisTextArea.get(1.0, END))
			file.close()
			#Change the window title
			self.__root.title(os.path.basename(self.__file) + " - Notepad")

	else:
		file = open(self.__file, "w")
		file.write(self.__thisTextArea.get(1.0, END))
		file.close()

def __cut(self):
	self.__thisTextArea.event_generate("<<Cut>>")

def __copy(self):
	self.__thisTextArea.event_generate("<<Copy>>")

def __paste(self):
	self.__thisTextArea.event_generate("<<Paste>>")




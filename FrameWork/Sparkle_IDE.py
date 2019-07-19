# Fur Script IDE
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.title("Fur Script IDE")

def Normal():
    text.config(font = ("FreeSans",12))

def Font():
    (triple,color) = askcolor()

    if(color):
        text.config(foreground=color)

def Kill():
    root.destroy()

def Open_File():
    text.delete(1.0, END)

    file = open(askopenfilename(), 'r')

    if(file != ''):
        Fur_Script = file.read()
        Fur_Script.insert(INSERT,fs)
    else:
        Parse_Sparkles_Buffer

def Save_File():
    filename = asksaveasfilename()

    if(filename):
        Script = text.get(1.0, END)
        open(filename, 'w').write(Script)


def Copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def Paste():
    try:
        clipboard_text = text.selection(selection='CLIPBOARD')
        text.insert(INSERT, clipboard_text)

    except:
        tkinter.messagebox.showerror("OwO", "OwO Clipboard Empty")

def Clear():
    Select = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)

def Clear_All():
    text.delete(1.0, END)

def Background():
    (triple,color) = askcolor()

    if(color):
        text.config(background=color)

def About():
    about_window = Toplevel(root)
    about_text = "\tFur Script IDE \t \n \tVersion 1.0.0 \t \n\n \tby steel99xl \t"
    about_label = Label(about_window,text=about_text,foreground='#eb8705')
    about_label.pack()

#Seting all the menues and crap

Menubar = Menu(root)




File_Menu = Menu(Menubar, tearoff = 0)
File_Menu.add_command(label = "Open...", command = Open_File)
File_Menu.add_command(label = "Save...", command = Save_File)
#File_Menu.add_seperator()
File_Menu.add_command(label = "Exit", command = Kill)

Mod_Menu = Menu(Menubar, tearoff = 0)
Mod_Menu.add_command(label = "Copy", command = Copy)
Mod_Menu.add_command(label = "Paste", command = Paste)
#Mod_Menu.add_separator()
Mod_Menu.add_command(label = "Clear Selection", command = Clear)
Mod_Menu.add_command(label = "Clear All", command = Clear_All)

Personalization_Menu =  Menu(Menubar, tearoff = 0)
Personalization_Menu.add_command(label = "Font", command = Font)
Personalization_Menu.add_command(label = "Background", command = Background)
#Personalization_Menu.add_seperator()
Personalization_Menu.add_command(label = "About", command = About)



Menubar.add_cascade(label = "File", menu = File_Menu)
Menubar.add_cascade(label = "Modification", menu = Mod_Menu)
Menubar.add_cascade(label = "Personalization", menu = Personalization_Menu)


text = Text(root, height=30, width=60, font = ("FreeSans", 12))

Scroll = Scrollbar(root, command = text.yview)
Scroll.config(command = text.yview)
text.config(yscrollcommand = Scroll.set)
Scroll.pack(side = RIGHT, fill = Y)
text.pack()

root.resizable(0,0)
root.config(menu = Menubar)
root.mainloop()

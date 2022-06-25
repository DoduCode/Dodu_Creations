from settings import *
import photo_editing
import os
import tkinter as tk
from tkinter import Entry, Button, StringVar, messagebox, colorchooser, filedialog
from tkinter.ttk import *
from PIL import Image
from shutil import copyfile

#custom save button
def open_file():
    if om1str.get() == 'Photo Editing':
        filename = filedialog.askopenfilename(initialdir = homeloc, title = 'Select Image', filetypes = [('Image Files', '*.jpg *.png *')])
        path = Path(filename)
        color.config(state = 'disabled')
        e1.delete(0, 'end')
        e1.insert(0, path.stem)
        width, height = Image.open(filename).size
        widthsize.delete(0, 'end')
        widthsize.insert(0, width)
        widthsize.config(state = 'disabled')
        heightsize.delete(0, 'end')
        heightsize.insert(0, height)
        heightsize.config(state = 'disabled')
        formatvar.set(path.suffix)
        b1.config(command = lambda: custom_save(filename))

    if om1str.get() == 'Type of Project':
        print('hi')
        messagebox.showerror("Error", 'Please select an option from the dropdown menu')

def custom_save(filelocation):
    os.chdir(projloc)
    try:
        if om1str.get() == 'Photo Editing':
            filename = e1.get() + ' - PhotoEditing'
            extension = formatvar.get()
            name = f'{e1.get()}{extension}'
            
            path = Path.cwd() / filename
            path.mkdir()
            os.chdir(filename)
            saveloc = Path.cwd() / name

            copyfile(filelocation, saveloc)

            os.chdir(homeloc)
            new.destroy() 
            photo_editing.setup(saveloc)
    
    except NameError:
        os.chdir(homeloc)
        new.destroy() 

##

def save():
    if len(e1.get()) == 0 or len(widthsize.get()) == 0 or len(heightsize.get()) == 0 or formatvar.get() == 'Extension':
        messagebox.showerror("Error", 'Please fill all the details')

    else:
        os.chdir(projloc)

        try:
            if om1str.get() == 'Photo Editing':
                filename = e1.get() + ' - PhotoEditing'
                width, height = int(widthsize.get()), int(heightsize.get())
                if stagewidthvar.get() == 'Inches':
                    width *= 96
                if stageheightvar.get() == 'Inches':
                    height *= 96
                    
                background = colorstr.get()
                extension = formatvar.get()
                name = f'{e1.get()}{extension}'
                
                path = Path.cwd() / filename
                path.mkdir()
                os.chdir(filename)

                image = Image.new(mode = 'RGB', size = (width, height), color = background)
                image.save(name)

                path = Path(os.getcwd())
                imgpath = Path.joinpath(path, name)

                os.chdir(homeloc)
                new.destroy() 
                photo_editing.setup(imgpath)
        
        except NameError:
            os.chdir(homeloc)
            new.destroy()             

def callback2(input1):
    if input1 == '/':
        return False

    elif input1 == "\\":
        return False

    elif input1 == '|':
        return False

    elif input1 == ':':
        return False

    elif input1 == '*':
        return False

    elif input1 == '?':
        return False

    elif input1 == '"':
        return False

    elif input1 == '<':
        return False

    elif input1 == '>':
        return False

def callback1(input1):
    if input1.isdigit():
        return True

    elif input1 == "":
        return True

    else:
        return False

def color_pick():
    stagecolor = colorchooser.askcolor(title = 'Stage Color')
    style = Style()
    style.configure('MINE.TButton', foreground = stagecolor[1], background = stagecolor[1])
    colorstr.set(stagecolor[1])

def change_color(choice):
    choice = colorstr.get()
    
    style = Style()
    style.configure('MINE.TButton', background = choice, foreground = choice, borderwidth = 0, focusthickness = 3, focuscolor = 'none')

def more_options(choice):
    global b1, colorstr, color, widthsize, heightsize, formatvar, stagewidthvar, stageheightvar

    choice = om1str.get()
    om1['menu'].entryconfigure(choice, state = 'disabled')

    if len(dislist) == 1:
        om1['menu'].entryconfigure(dislist[0], state = 'normal')
        dislist.pop(0)
        dislist.append(choice)

    else:
        dislist.append(choice)
    
    if choice == 'Photo Editing':
        for widgets in new.winfo_children():
            if widgets.winfo_class() == 'new' or widgets.winfo_class() == 'Button':
                widgets.destroy()

        f1 = Frame(new)
        f1.pack(side = 'top', expand = True, fill = 'x')
        
        width = Label(f1, text = 'Width of Stage: ')
        widthsize = Entry(f1, width = 15)
        stagewidthvar = StringVar()
        stagewidth = OptionMenu(f1, stagewidthvar, 'Pixels', 'Pixels', 'Inches')

        height = Label(f1, text = 'Height of Stage: ')
        heightsize = Entry(f1, width = 15)
        stageheightvar = StringVar()
        stageheight = OptionMenu(f1, stageheightvar, 'Pixels', 'Pixels', 'Inches')

        formatvar = StringVar()
        dropdown = OptionMenu(f1, formatvar, 'Extension', '.png', '.jpeg')

        l1 = Label(f1, text = 'Stage Background:')
        colorstr = StringVar()
        colorstr.set('White')
        color = OptionMenu(f1, colorstr, 'White', 'White', 'Red', 'Magenta', 'Green', 'Blue', 'Cyan', 'Yellow', 'Orange', 'Gray', 'Black', command = change_color)
        custcolbg = Label(f1, text = '', borderwidth = 2)
        customcolor = Button(f1, text = '', command = color_pick, style = 'MINE.TButton')
        
        b1 = Button(new, text = 'Create', command = save)

        width.grid(row = 0, column = 0)
        widthsize.grid(row = 0, column = 1)
        reg = f1.register(callback1)
        widthsize.config(validate = 'key', validatecommand = (reg, '%P'))
        stagewidth.grid(row = 0, column = 2)

        height.grid(row = 1, column = 0)
        heightsize.grid(row = 1, column = 1)
        reg = f1.register(callback1)
        heightsize.config(validate = 'key', validatecommand = (reg, '%P'))
        stageheight.grid(row = 1, column = 2)

        l1.grid(row = 2, column = 0)
        color.grid(row = 2, column = 1)
        color.config(width = 12)
        custcolbg.grid(row = 2, column = 2, ipadx = 22, ipady = 2)
        customcolor.grid(row = 2, column = 2, ipadx = 20)
        dropdown.grid(row = 3, column = 0 )
        b1.pack(ipady = 10, side = 'bottom' , expand = False, fill = 'x')

    if choice == 'Video Editing':
        for widgets in new.winfo_children():
            if widgets.winfo_class() == 'TFrame' or widgets.winfo_class() == 'TButton':
                widgets.destroy()

def ask():
    global dislist, om1, om1str, e1

    l1 = Label(new, text = 'Name: ')
    e1 = Entry(new, width = 35)
    b1 = Button(new, text = '...', command = open_file)

    om1str = StringVar()
    om1list = ['Type of Project', 'Photo Editing', 'Video Editing']
    om1 = OptionMenu(new, om1str, *om1list, command = more_options)

    dislist = []

    l1.place(x = 5, y = 5)
    e1.place(x = 50, y = 5)
    reg = new.register(callback2)
    e1.config(validate = 'key', validatecommand = (reg, '%P'))
    b1.place(x = 275, y = 4)
    om1.place(x = 5, y = 40)

def setup():
    global new

    new = tk.Toplevel()
    new.geometry('350x400')
    new.title('Create New Project')
    new.resizable(False, False)
    ask()

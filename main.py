from settings import *
from create_new import setup
from latest_projects import latestproj, openproj
from threading import Thread
from tkinter import W, Canvas, PhotoImage
from tkinter.ttk import * 

def home():
    global menuframe, nameframe

    for children in root.winfo_children():
        children.destroy()
    
    nameframe = Frame(root, style = 'LIGHTFRAMES.TFrame', height = 20)
    nameframe.pack(side = 'top', expand = False, fill = 'x')
    menuframe = Frame(root, width = menuframewidth, style = 'LIGHTFRAMES.TFrame')
    menuframe.pack(side = 'left', expand = False, fill = 'y')
    menuframe.pack_propagate(0)
    infoframe = Frame(root, height = infoframeheight, style = 'FRAMES.TFrame')
    infoframe.pack(side = 'top', expand = False, fill = 'x')
    infoframe.pack_propagate(0)
    projectsframe = Frame(root, style = 'FRAMES.TFrame')
    projectsframe.pack(side = 'top', expand = False, fill = 'x')
    projholder = Frame(projectsframe, style = 'FRAMES.TFrame', height = fit_to_height_latest_proj)
    projholder.pack(side = 'top', expand = True, fill = 'x')
    projholder.pack_propagate(0)

    l1 = Label(nameframe, text = 'Creations', font = ('Arial', 15), style = 'LIGHTLABELBG.TLabel')
    l2 = Label(infoframe, image = test)

    homepage = Button(menuframe, text = '', command = home)
    learning = Button(menuframe, text = 'Learn', command = learn)
    createproj = Button(menuframe, text = 'Create Project', command = setup)
    openproj = Button(menuframe, text = 'Open Project', command = open_projects)

    thread = Thread(target = latestproj, args = (projholder,))
    thread.start()

    l1.pack(anchor = W)
    l2.pack(side = 'top', anchor = 'center', expand = True)
    homepage.pack(anchor = W, padx = 10, pady = 5)
    learning.pack(anchor = W, padx = 10, pady = (2, 20))
    createproj.pack(anchor = W, padx = 10, pady = 5)
    openproj.pack(anchor = W, padx = 10, pady = 5)

    homepage.config(text = 'home')
    
def learn():
    for child in root.winfo_children():
        if child == menuframe:
            pass

        elif child == nameframe:
            pass

        else:
            child.destroy()

def open_projects():
    for child in root.winfo_children():
        if child == menuframe:
            pass

        elif child == nameframe:
            pass

        else:
            child.destroy()

    main_frame = Frame(root, height = fit_to_height_open_proj, style = 'FRAMES.TFrame')
    main_frame.pack(side = 'top', expand = True, fill = 'x')
    main_frame.pack_propagate(0)

    canvas = Canvas(main_frame)
    canvas.pack(side = 'left', fill = 'both', expand = 1)

    sb1 = Scrollbar(main_frame, orient = 'vertical', command = canvas.yview)
    sb1.pack(side = 'right', fill = 'y')

    canvas.config(yscrollcommand = sb1.set)
    canvas.bind('<Configure>', lambda e: canvas.config(scrollregion = canvas.bbox('all')))

    projholder = Frame(canvas, style = 'FRAMES.TFrame')   
    canvas.create_window((0, 0), window = projholder, anchor = 'center')

    thread = Thread(target = openproj, args = (projholder,))
    thread.start()

test = PhotoImage(file = fileloc)

home()
root.mainloop()
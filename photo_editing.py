from settings import *
import os
from photo_editing_filter import show_filters
from tkinter import colorchooser, Canvas, Scrollbar, N
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageGrab
import keyboard

def save(stageframe, filelocation):
    x=root.winfo_rootx()+stageframe.winfo_x()+stage.winfo_x()
    y=root.winfo_rooty()+stageframe.winfo_y()+stage.winfo_y()
    x1=x+stage.winfo_width()
    y1=y+stage.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(filelocation)

def type_of(color):
    type_pen = 'marker'
    if type_pen == 'marker':
        pencil_motion_marker(color = color)

#pixel pen
def pencil_motion_marker(color):
    stage.bind('<Button-1>', get_pos_marker)
    stage.bind('<B1-Motion>', lambda event, color = color: pencil_draw_marker(event, color))

def get_pos_marker(event):
    global lastx, lasty
    
    lastx, lasty = event.x, event.y

def pencil_draw_marker(event, color):
    stage.create_line((lastx, lasty, event.x, event.y), width = width.get(), fill = color, capstyle = 'round', smooth = True)
    get_pos_marker(event)

def choose_pen_color():
    pencilcolor = colorchooser.askcolor(title = 'Pencil Color')
    type_of(pencilcolor[1])

##
        
def pencil_click():
    global width, opacity

    Whitepencolb = Button(optionsframe, image = Whitepencolimg, style = 'COLBG.TButton', command = lambda m = 'White': type_of(m))
    Whitepencolb.grid(row = 0, column = 0, padx = 10, pady = 1)
    
    Redpencolb = Button(optionsframe, image = Redpencolimg, style = 'COLBG.TButton', command = lambda m = 'Red': type_of(m))
    Redpencolb.grid(row = 1, column = 0, padx = 10, pady = 1)
    
    Magentapencolb = Button(optionsframe, image = Magentapencolimg, style = 'COLBG.TButton', command = lambda m = 'Magenta': type_of(m))
    Magentapencolb.grid(row = 0, column = 1, padx = 10, pady = 1)

    Limegreenpencolb = Button(optionsframe, image = Limegreenpencolimg, style = 'COLBG.TButton', command = lambda m = 'Lime': type_of(m))
    Limegreenpencolb.grid(row = 1, column = 1, padx = 10, pady = 1)
    
    Greenpencolb = Button(optionsframe, image = Greenpencolimg, style = 'COLBG.TButton', command = lambda m = 'Green': type_of(m))
    Greenpencolb.grid(row = 0, column = 2, padx = 10, pady = 1)
    
    Bluepencolb = Button(optionsframe, image = Bluepencolimg, style = 'COLBG.TButton', command = lambda m = 'Blue': type_of(m))
    Bluepencolb.grid(row = 1, column = 2, padx = 10, pady = 1)
    
    Cyanpencolb = Button(optionsframe, image = Cyanpencolimg, style = 'COLBG.TButton', command = lambda m = 'Cyan': type_of(m))
    Cyanpencolb.grid(row = 0, column = 3, padx = 10, pady = 1)
    
    Yellowpencolb = Button(optionsframe, image = Yellowpencolimg, style = 'COLBG.TButton', command = lambda m = 'Yellow': type_of(m))
    Yellowpencolb.grid(row = 1, column = 3, padx = 10, pady = 1)

    Orangepencolb = Button(optionsframe, image = Orangepencolimg, style = 'COLBG.TButton', command = lambda m = 'Orange': type_of(m))
    Orangepencolb.grid(row = 0, column = 4, padx = 10, pady = 1)

    Graypencolb = Button(optionsframe, image = Graypencolimg, style = 'COLBG.TButton', command = lambda m = 'Gray': type_of(m))
    Graypencolb.grid(row = 1, column = 4, padx = 10, pady = 1)

    Blackpencolb = Button(optionsframe, image = Blackpencolimg, style = 'COLBG.TButton', command = lambda m = 'Black': type_of(m))
    Blackpencolb.grid(row = 0, column = 5, padx = 10, pady = 1)

    Createnewpencolb = Button(optionsframe, image = Createnewpencolimg, style = 'COLBG.TButton', command = choose_pen_color)
    Createnewpencolb.grid(row = 1, column = 5, padx = 10, pady = 1)

    widthlabel = Label(optionsframe, text = 'Width: ', style = 'LABELBG.TLabel')
    width = Scale(optionsframe, from_ = 1, to = 20, style = 'SCALEBG.Horizontal.TScale')
    widthlabel.grid(row = 0, column = 6)
    width.grid(row = 0, column = 7)
    width.set(20)

    opacitylabel = Label(optionsframe, text = 'Opacity: ', style = 'LABELBG.TLabel')
    opacity = Scale(optionsframe, from_ = 0, to = 1.0, style = 'SCALEBG.Horizontal.TScale')
    opacitylabel.grid(row = 1, column = 6)
    opacity.grid(row = 1, column = 7)
    opacity.set(1.0)
  
def stageresize(event):
    x = event.width/2  
    y = event.height/2
    stage.coords(img_id, x, y) 

def setup(filelocation):
    global stage, img_id, optionsframe, draw
    
    for widgets in root.winfo_children():
        widgets.destroy()

    root.config(bg = '#454545')
    iconsframewidth = int(screen_width / 20)
    
    frames = Style()
    frames.configure('FRAMES.TFrame', background = '#2a2a2a')
    sep = Style()
    sep.configure('SEP.TFrame', background = '#1a1a1a')
    style = Style()
    style.configure('STAGE.TFrame', background = '#454545')
    icon = Style()
    icon.configure('ICON.TButton', background = '#2a2a2a', foreground = '#2a2a2a')
    
    iconsframe = Frame(root, width = iconsframewidth, style = 'FRAMES.TFrame')
    iconsframe.pack(side = 'left', expand = False, fill = 'y')
    iconsframe.pack_propagate(0)
    sep1frame = Frame(root, style = 'SEP.TFrame', width = 5)
    sep1frame.pack(side = 'left', expand = False, fill = 'y')
    optionsframe = Frame(root, style = 'FRAMES.TFrame', height = 100)
    optionsframe.pack(side = 'top', expand = False, fill = 'x')
    optionsframe.pack_propagate(0)
    sep2frame = Frame(root, style = 'SEP.TFrame', height = 5)
    sep2frame.pack(side = 'top', expand = False, fill = 'x')
    propertyframe = Frame(root, style = 'FRAMES.TFrame', width = 150)
    propertyframe.pack(side = 'right', expand = False, fill = 'y')
    propertyframe.pack_propagate(0)
    sep3frame = Frame(root, style = 'SEP.TFrame', width = 5)
    sep3frame.pack(side = 'right', expand = False, fill = 'y')
    stageframe = Frame(root, style = 'STAGE.TFrame')
    stageframe.pack(side = 'top', expand = True, fill = 'both')
    stageframe.pack_propagate(0)

    path = Path(filelocation)
    changedir = path.parent
    os.chdir(changedir)

    image = Image.open(path.name)
    width, height = image.size

    stage = Canvas(stageframe, width = width, height = height, bd = 0, highlightthickness = 0, relief = 'flat')

    hbar = Scrollbar(stageframe, orient = 'horizontal')
    hbar.pack(side = 'bottom', fill = 'x')
    hbar.config(command = stage.xview)
    vbar = Scrollbar(stageframe, orient = 'vertical')
    vbar.pack(side = 'right', fill = 'y')
    vbar.config(command = stage.yview)
    stage.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set, scrollregion = stage.bbox('all'))
    stage.pack(side="top", anchor = 'c', expand=True)

    root.update()

    keyboard.add_hotkey("ctrl+s", lambda stageframe = stageframe, filelocation = filelocation: save(stageframe, filelocation))

    pencilbutton = Button(iconsframe, image = pencilimg, command = pencil_click, style = 'ICON.TButton')
    pencilbutton.pack(anchor = N, pady = 10)

    filterbutton = Button(iconsframe, image = filterimg, command = lambda m = path.name, path = filelocation: show_filters(m, path), style = 'ICON.TButton')
    filterbutton.pack(anchor = N, pady = 10)

    imgtk = ImageTk.PhotoImage(Image.open(filelocation)) 
    img_id = stage.create_image(stage.winfo_width() / 2, stage.winfo_height() / 2, image = imgtk)
    stage.image = imgtk
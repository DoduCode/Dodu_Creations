from pathlib import Path
import tkinter as tk
from tkinter import PhotoImage
from tkinter.ttk import Style

#Tk window
root = tk.Tk()
root.title('Dodu Creations')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

w = 1150
h = 600
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.minsize(1150, 600)

menuframewidth = int(screen_width / 10)
infoframeheight = int(screen_width / 3)
fit_to_height_latest_proj = int(screen_height - infoframeheight)
fit_to_height_open_proj = int(screen_height - 20)

#Paths to files
homeloc = Path(__file__).parent.resolve()
creationloc = homeloc / 'Creation Folders'
projloc = creationloc / 'Projects'
imgloc = creationloc / 'img'

#img files
iconsloc = imgloc / 'Icons'
penimgloc = iconsloc / 'Pencil Icons'

fileloc = imgloc / 'test.png'

#icons
pencil = iconsloc / 'pencil_draw.png'
filter = iconsloc / 'filter.png'

#pencilcolors
Whitepencol = penimgloc / 'White.png'
Redpencol = penimgloc / 'Red.png'
Magentapencol = penimgloc / 'Magenta.png'
Greenpencol = penimgloc / 'Green.png'
Limegreenpencol = penimgloc / 'Limegreen.png'
Bluepencol = penimgloc / 'Blue.png'
Cyanpencol = penimgloc / 'Cyan.png'
Yellowpencol = penimgloc / 'Yellow.png'
Orangepencol = penimgloc / 'Orange.png'
Graypencol = penimgloc / 'Gray.png'
Blackpencol = penimgloc / 'Black.png'
Createnewpencol = penimgloc / 'Createnew.png'

#making all the images usable
pencilimg = PhotoImage(file = pencil)
filterimg = PhotoImage(file = filter)
Whitepencolimg = PhotoImage(file = Whitepencol)
Redpencolimg = PhotoImage(file = Redpencol)
Magentapencolimg = PhotoImage(file = Magentapencol)
Greenpencolimg = PhotoImage(file = Greenpencol)
Limegreenpencolimg = PhotoImage(file = Limegreenpencol)
Bluepencolimg = PhotoImage(file = Bluepencol)
Cyanpencolimg = PhotoImage(file = Cyanpencol)
Yellowpencolimg = PhotoImage(file = Yellowpencol)
Orangepencolimg = PhotoImage(file = Orangepencol)
Graypencolimg = PhotoImage(file = Graypencol)
Blackpencolimg = PhotoImage(file = Blackpencol)
Createnewpencolimg = PhotoImage(file = Createnewpencol)

#theme
style = Style()
style.configure('COLBG.TButton', foreground = '#2a2a2a', background = '#2a2a2a')

style = Style()
style.configure('LIGHT.TButton', foreground = '#454545', background = '#454545')

style = Style()
style.configure('SCALEBG.Horizontal.TScale', background = '#2a2a2a')

style = Style()
style.configure('LABELBG.TLabel', foreground = '#c3c3c3', background = '#2a2a2a')

style = Style()
style.configure('LIGHTLABELBG.TLabel', foreground = '#c3c3c3', background = '#454545')

style = Style()
style.configure('FRAMES.TFrame', background = '#2a2a2a')

style = Style()
style.configure('LIGHTFRAMES.TFrame', background = '#454545')

style = Style()
style.configure('SEP.TFrame', background = '#1a1a1a')

style = Style()
style.configure('STAGE.TFrame', background = '#454545')

style = Style()
style.configure('ICON.TButton', background = '#2a2a2a', foreground = '#2a2a2a')
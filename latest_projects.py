from settings import *
from photo_editing import setup
import os
from pathlib import Path
import datetime
from tkinter import *
from tkinter.ttk import *

def openproj(frame):
    list_of_dirs_to_exclude = []
    list_of_dirs = []
    max_mtime = 0
    for dirs in os.listdir(projloc):
        list_of_dirs.insert(0, dirs)

    while len(list_of_dirs) != 5: 
        for root, dirs, files in os.walk(projloc):
            if root not in list_of_dirs_to_exclude:
                for fname in files:
                    full_path = os.path.join(root, fname)
                    mtime = os.stat(full_path).st_mtime
                    if mtime > max_mtime:
                        max_mtime = mtime
                        max_dir = root
                        #max_file = fname
                        path = Path(full_path)
                        time_created = datetime.datetime.fromtimestamp(os.stat(path).st_ctime)
                        size = os.stat(path).st_size

        list_of_dirs_to_exclude.insert(0, max_dir)
        fullname = path.stem

        if path.suffix == '.png' or path.suffix == '.jpg' or path.suffix == '.jpeg':
            projtype = 'PhotoEditing'
            size = int(size / 1024)
            size = f'{size} kb'

        else:
            pass

        if len(fullname) >= 20:
            name = f'{fullname[0:17]}...'

        else:
            length_to_add = 26 - len(fullname)
            total_spaces = ' ' * length_to_add
            name = f'{fullname}{total_spaces}'

        time_created = time_created.strftime('%Y-%m-%D %I:%M:%S %p')
        b1 = Button(frame, text = f'Name: {name}\t\t Project Type: {projtype}\t\t Size: {size}\t\t Date Created: {time_created}', command = lambda m = path: setup(m), style = 'LIGHT.TButton', width = 150)
        b1.pack(anchor = CENTER, pady = 5)

        max_mtime = 0

        if len(list_of_dirs_to_exclude) == len(list_of_dirs):
            break

def latestproj(frame):
    try:
        list_of_dirs_to_exclude = []
        list_of_dirs = []
        max_mtime = 0
        for dirs in os.listdir(projloc):
            list_of_dirs.insert(0, dirs)

        while len(list_of_dirs) != 5: 
            for root, dirs, files in os.walk(projloc):
                if root not in list_of_dirs_to_exclude:
                    for fname in files:
                        full_path = os.path.join(root, fname)
                        mtime = os.stat(full_path).st_mtime
                        if mtime > max_mtime:
                            max_mtime = mtime
                            max_dir = root
                            #max_file = fname
                            path = Path(full_path)
                            time_created = datetime.datetime.fromtimestamp(os.stat(path).st_ctime)
                            size = os.stat(path).st_size

            list_of_dirs_to_exclude.insert(0, max_dir)
            fullname = path.stem

            if path.suffix == '.png':
                projtype = 'PhotoEditing'
                size = int(size / 1024)
                size = f'{size} kb'

            if path.suffix == '.jpg' or path.suffix == '.jpeg':
                projtype = 'PhotoEditing'
                size = int(size / 1024)
                size = f'{size} kb'

            if len(fullname) >= 20:
                name = f'{fullname[0:17]}...'

            else:
                length_to_add = 26 - len(fullname)
                total_spaces = ' ' * length_to_add
                name = f'{fullname}{total_spaces}'

            time_created = time_created.strftime('%Y-%m-%D %I:%M:%S %p')
            b1 = Button(frame, text = f'Name: {name}\t\t Project Type: {projtype}\t\t Size: {size}\t\t Date Created: {time_created}', command = lambda m = path: setup(m), style = 'LIGHT.TButton', width = 150)
            b1.pack(anchor = CENTER, pady = 5)

            max_mtime = 0

            if len(list_of_dirs_to_exclude) == 6:
                break

    except UnboundLocalError:
        pass
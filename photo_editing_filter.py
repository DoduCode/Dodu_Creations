import cv2
import os
import tkinter as tk
from tkinter.ttk import Button
from cv2 import imread

def water_color(image, path):
    image = imread(image)
    watercolor = cv2.stylization(image, sigma_s=60, sigma_r=0.6)
    cv2.imshow("Water Color", watercolor)
    cv2.imwrite(path, watercolor)

def sketch_pencil(image, path):
    image = imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Sketch", pencil_sketch)
    cv2.imwrite(path, pencil_sketch)      

def show_filters(image, path):
    print(os.getcwd())
    filter = tk.Toplevel()
    filter.geometry('350x400')
    filter.title('Apply Filter')
    filter.resizable(False, False)

    pencilsketch = Button(filter, text = 'Pencil Sketch', command = lambda m = image, path = path: sketch_pencil(m, path))
    watercolor = Button(filter, text = 'Water Color', command = lambda m = image, path = path: water_color(m, path))

    pencilsketch.pack()
    watercolor.pack()
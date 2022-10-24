from glob import glob
from importlib.resources import path
from select import select
from tkinter import filedialog
from rembg import remove
from PIL import Image
from tkinter import *
import glob

#section barre de menu
files = glob.glob("images/*.jpg")
len(files)
#fonctiion de selection fichier

    
for file in files:
    input_path = file
    output_path = input_path.replace('images','result')
    
    with open(input_path, 'rb') as i:
        with open(output_path,'wb') as o:
            original_image = i.read()
            output= remove(original_image)
            o.write(output)

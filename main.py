from importlib.resources import path
from select import select
from tkinter import filedialog
from rembg import remove
from PIL import Image
from tkinter import *


#section barre de menu

#fonctiion de selection fichier

    

output_path = 'output.png'

input =Image.open("trtrt.jpg")
output = remove(input)
output.save(output_path)


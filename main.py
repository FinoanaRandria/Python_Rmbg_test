from importlib.resources import path
from rembg import remove
from PIL import Image
from tkinter import *


input_path = 'cl.jpg'
output_path = 'output.png'

input =Image.open(input_path)
output = remove(input)
output.save(output_path)
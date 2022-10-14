from importlib.resources import path
from rembg import remove
from PIL import Image
from tkinter import *

root = Tk()

root.title("RemoveBGPython")
root.geometry('700x600')
root.minsize(300,220)
#section barre de menu
menu_barr =Menu(root,bg="white")
input_path = 'cl.jpg'
output_path = 'output.png'

#input =Image.open(input_path)
#output = remove(input)
#output.save(output_path)

root.mainloop()
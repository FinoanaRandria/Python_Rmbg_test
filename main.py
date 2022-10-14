from importlib.resources import path
from select import select
from tkinter import filedialog
from rembg import remove
from PIL import Image
from tkinter import *

root = Tk()

root.title("RemoveBGPython")
root.geometry('700x600')
root.minsize(300,220)
#section barre de menu
menu_barr =Menu(root,bg="white")

#fonctiion de selection fichier
def jpg() :
    file = filedialog.askopenfilename(initialdir="/")
    
    
selectfile =Button(root,bg="orange",border=0,text="select file" ,command=jpg).pack(expand=YES)
#input_path = 'cl.jpg'
#output_path = 'output.png'

#input =Image.open(input_path)
#output = remove(input)
#output.save(output_path)

root.mainloop()

from asyncio import streams
from rembg import remove
import PIL
import io
import glob
#run

#section barre de menu
files = glob.glob("images/*.jpg")
len(files)
#fonctiion de selection fichier

    
for file in files:
    input_path = file
    output_path = input_path.replace('images','results')
    
    with open(input_path, 'rb') as i:
        with open(output_path,'wb') as o:
            original_image = i.read()
            output= remove(original_image)
            o.write(output)

import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

Tk().withdraw()
print("Choose an image: ")
filename = askopenfilename()
print("Select a folder where you want to save the resized image: ")
filedirectory = askdirectory()
newfilename = input("Enter new file name: ")
fullfilename, extn = os.path.splitext(filename)
img = Image.open(filename)
print("Image dimensions are: "+str(img.size))
size = tuple(int(x.strip())for x in input("Enter new dimensions: ").split(','))
img_resized = img.resize(size, Image.LANCZOS)
print("Image resized to"+" "+str(size))
print("Your resized image is saved in: "+filedirectory)
img_resized.save(filedirectory+"/"+newfilename+" "+str(size)+"."+extn)
e = input("press Enter key to exit... Until next time... ciao!")

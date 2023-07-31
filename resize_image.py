from PIL import Image
from tkinter.filedialog import *

link = askopenfilename()

image = Image.open(link)

print(f"Current size : {image.size}")

print("what size do you want to save (x*y) ?")
print("type the value of x :")
x = int(input())
print("type the value of y :")
y = int(input())
resized_image = image.resize((x,y))

resized_image.save('resized_image.png')

print("successfully resized")
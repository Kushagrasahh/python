import random

from PIL import Image


b=["rock" ,"paper","scissors"]
a= random .choice(b)
print (a)

pic="r\\"+  a  +".png"
im=Image.open(pic)
im.show()

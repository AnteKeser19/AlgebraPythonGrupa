from PIL import Image, ImageDraw

img=Image.open('Algebra_campus.jpg')

img_draw=ImageDraw.Draw(img) #pozadina za iscrtavanja

#img_draw.rectangle((800,500,3400,2200),fill=None,outline='red',width=5)
img.show()

img_draw.ellipse((800,500,2500,2200),fill=None,outline=(120,0,111),width=5)
img.show()

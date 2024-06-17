from PIL import Image, ImageEnhance

img=Image.open('Algebra_campus.jpg')

img_enh1=ImageEnhance.Brightness(img)
#img_enh1.enhance(0.25).show()

img_enh2=ImageEnhance.Contrast(img)
#img_enh2.enhance(4).show()

img_enh3=ImageEnhance.Sharpness(img)
#img_enh3.enhance(6).show()

img_enh4=ImageEnhance.Color(img)
img_enh4.enhance(6).show()


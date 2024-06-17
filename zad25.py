from PIL import Image

foto_putanja='Algebra_campus.jpg'

foto_var=Image.open(foto_putanja)

print(foto_var.size)

# crop uzima left, up, right, down kao tocke
#0,0
#########
#       #
#       #
#########Xmax-1, Ymax-1

lijevo=0+500
gore=0+500
desno=foto_var.size[0]-500
dolje=foto_var.size[1]-500
try:
    foto_crop=foto_var.crop((lijevo,gore,desno,dolje))
except:
    foto_crop=foto_var

foto_crop.save('Algebra_campus_crop.jpg','JPEG')
foto_crop.save('Algebra_campus_crop.png','PNG')


foto_var.show()
foto_crop.show()
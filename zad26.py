from PIL import Image

foto_putanja='Algebra_campus.jpg'

foto_var=Image.open(foto_putanja)

foto_convert=foto_var.convert(mode='L')

foto_convert.save('Algebra_camous_convert.jpg','JPEG')

foto_convert.show()
# python3 -m pip install pillow

from PIL import Image

foto_putanja='Algebra_campus.jpg'
foto_var=Image.open(foto_putanja)
print(foto_var)
print()
print(f'Format slike: {foto_var.format}')
print(f'Mod slike: {foto_var.mode}')
print(f'Dimenzije slike: {foto_var.size}')
print()
print(f'X velicina: {foto_var.size[0]} - Y velicina: {foto_var.size[1]}')

foto_var.show()
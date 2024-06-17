from PIL import Image

foto_source=Image.open('Python_logo_and_wordmark.png')
foto_destination=Image.open('Algebra_campus.jpg')

print(foto_source.size)
print(foto_destination.size)

foto_source=foto_source.convert('RGBA')

foto_destination.paste(foto_source,(500,300))
foto_destination.show()
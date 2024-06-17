from PIL import Image, ImageFilter

img=Image.open('Algebra_campus.jpg')

#img01=img.filter(ImageFilter.CONTOUR).show()
#img02=img.filter(ImageFilter.EDGE_ENHANCE).show()
#img03=img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
#img04=img.filter(ImageFilter.EMBOSS).show()
#img05=img.filter(ImageFilter.FIND_EDGES).show()
#img06=img.filter(ImageFilter.SHARPEN).show()
#img07=img.filter(ImageFilter.SMOOTH).show()
#img08=img.filter(ImageFilter.SMOOTH_MORE).show()

#img09=img.filter(ImageFilter.BoxBlur(radius=3)).show()
#img10=img.filter(ImageFilter.BoxBlur(radius=10)).show()
#img11=img.filter(ImageFilter.GaussianBlur(radius=8)).show()
#img12=img.filter(ImageFilter.UnsharpMask(radius=17,percent=250,threshold=3)).show()
#img13=img.filter(ImageFilter.MaxFilter(size=17)).show()
#img14=img.filter(ImageFilter.MedianFilter(size=7)).show()
img14=img.filter(ImageFilter.MinFilter(size=7)).show()
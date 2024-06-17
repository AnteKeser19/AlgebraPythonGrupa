from PIL import Image

foto=Image.open('Algebra_campus.jpg')

#transpose

#foto_flipTB=foto.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
#foto_flipLR=foto.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
#foto_rotate90=foto.transpose(Image.Transpose.ROTATE_90).show()
#foto_rotate180=foto.transpose(Image.Transpose.ROTATE_180).show()
#foto_rotate270=foto.transpose(Image.Transpose.ROTATE_270).show()
#foto_transpose=foto.transpose(Image.Transpose.TRANSPOSE).show()
foto_transverse=foto.transpose(Image.Transpose.TRANSVERSE).show()
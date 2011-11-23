import ImageFilter
import Image

im=Image.open("784_1.jpg")
im=im.filter(ImageFilter.FIND_EDGES)
im.show()



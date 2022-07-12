#library
from PIL import Image, ImageFilter

#open image
before = Image.open("courtyard.bmp")

#apply filter to image
after = before.filter(ImageFilter.BLUR)

#save newimage into a new file
after.save("out.bmp")


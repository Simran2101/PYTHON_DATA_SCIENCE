from PIL import Image, ImageFilter, ImageEnhance # <--------2 classes added

im = Image.open('tiger.jpg') #relative address
im2 = Image.open(r'C:\Users\hp\Pictures\cab.jpg')

#im.filter(ImageFilter.FIND_EDGES).show()
#im.filter(ImageFilter.BLUR).show()
#im.filter(ImageFilter.SMOOTH).show()
#im.filter(ImageFilter.SHARPEN).show()
#im.filter(ImageFilter.MaxFilter(3)).show() #highlight whites
#im.filter(ImageFilter.MinFilter(3)).show() #highlight black
#im.filter(ImageFilter.MedianFilter(5)).show() #highlight greys
#im.filter(ImageFilter.GaussianBlur(40)).save('carrots_blurred.jpg')

#eim = ImageEnhance.Color(im)
#for i in range(-10,11,2):
#   eim.enhance(i).show()

im2_s = im2.resize((320,240))
imc.paste(im2_s, (700,0))
imc.paste(im2_s, (700,0))
imc.show()
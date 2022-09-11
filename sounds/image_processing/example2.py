from PIL import Image

im = Image.open('carrots.jpg') #relative address
im2 = Image.open(r'C:\Users\hp\Pictures\cab.jpg')

print('resolution' ,im.size)
print('height' ,im2)
print('width' ,im.width)
print('mode' ,im.mode)
print('format' , im.format)
print('exif' ,im.info)

im.convert('L').show()
im.resize((100,100)).show()
im.resize((im.width * 5, im.height * 5)).show()
im.resize((im.width * 5, im.height * 5)).save('carrots_5x.jpg')
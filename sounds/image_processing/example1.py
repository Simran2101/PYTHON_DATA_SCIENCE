from PIL import Image

im = Image.open('carrots.jpg') #relative address
im2 = Image.open(r'C:\Users\hp\Pictures\cab.jpg')

print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()
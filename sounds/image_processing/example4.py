from PIL import Image,ImageDraw, ImageFont # <--------2 classes added

im = Image.open('carrots.jpg') #relative address
im2 = Image.open(r'C:\Users\hp\Pictures\cab.jpg')

font = ImageFont.truetype(r'C:\Windows\Fonts\ARLRDBD.TTF', 140)
font2 = ImageFont.truetype(r'C:\Windows\Fonts\ARLRDBD.TTF', 40)

imd = ImageDraw.Draw(im)

imd.text((200,100), 'Carrots',fill=(255,150,0), font=font)
imd.text((700,700), 'Rs. 100.00',fill=(0,0,0), font=font2)
im.save('edited_carrot.jpg')
im.show()

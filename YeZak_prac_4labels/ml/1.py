from PIL import Image, ImageDraw, ImageFilter

def image_merge(im1):

im1 = Image.open('./pastel_interiopr2.jpg')
im2 = Image.open('./1.jpg')

# resize input 넣어줘야함

back_im = im1.copy()
back_im.paste(im2, (375, 450))
back_im.save('./result.jpg', quality=95) #output

# return
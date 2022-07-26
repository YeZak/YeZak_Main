from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('./interior2/pastel_interiopr2.jpg')
im2 = Image.open('./clip_test_image/modern_impressionism9.jpg.jpg')

# resize input 넣어줘야함
back_im = im1.copy()
back_im.paste(im2, (375, 450))
back_im.save('./result.jpg', quality=95) #output
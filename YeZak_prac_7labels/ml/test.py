from CLIP_func import mktag
from CLIP_model import CLIP_tag
import skimage.io as io
import PIL.Image

image = io.imread(
    "../clip_test_image/modern_impressionism35.jpg")
io.imshow(image)
#io.show()

#tag = CLIP_tag(image, Is_path = False)

#print(tag)


def image_merge(image, label_num, Is_path=False ):
    if (Is_path):
        image = io.imread(image)

    image = PIL.Image.fromarray(image)

    if label_num == 0:  # ORIENTALISM
        im1 = PIL.Image.open('../wall2/warm_wall.jpg')
    elif label_num == 1:  # REALISM
        im1 = PIL.Image.open('../wall2/palace_wall.jpg')
    elif label_num == 2:  # ANIMATION
        im1 = PIL.Image.open('../wall2/warm_wall.jpg')
    elif label_num == 3:  # PENCIL_DRAWING
        im1 = PIL.Image.open('../wall2/black_wall.jpg')
    elif label_num == 4:  # IMPRESSIONISM
        im1 = PIL.Image.open('../wall2/pastel_wall.jpg')
    elif label_num == 5:  # ABSTRACT
        im1 = PIL.Image.open('../wall2/primary_wall.jpg')
    elif label_num == 6:  # POP_ART
        im1 = PIL.Image.open('../wall2/primary_wall.jpg')

    image_resized = image.resize((240,int(240/image.size[0]*image.size[1])))
    # image_resized.save('./image_resized.jpg', quality=95) #output1
    back_im = im1.copy() # background
    back_im.paste(image_resized, (380, 400)) # image_resized 된거를 back_im에 붙여넣는다. (380, 400) 은 좌표값
    # back_im.save('./result.jpg', quality=95) #output2

    return image_resized, back_im

image, back_im = image_merge(image, label_num = 4, Is_path = False)

back_im.show()
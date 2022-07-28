
import skimage.io as io
import PIL.Image
import pymysql
import os
import os

import random
import string

from media import interior

from yezak.settings import MEDIA_ROOT

from yezak.settings import BASE_DIR





def image_merge(image, label_num, Is_path=False ):

    n = 10  # 문자의 개수(문자열의 크기)
    rand_str = ""  # 문자열

    for i in range(n):
        rand_str += str(random.choice(string.ascii_uppercase + string.digits))

    if (Is_path):
        image = io.imread(image)

    image = PIL.Image.fromarray(image)

    if label_num == 0:  # ORIENTALISM
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/warm_wall.jpg')
    elif label_num == 1:  # REALISM
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/palace_wall.jpg')
    elif label_num == 2:  # ANIMATION
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/warm_wall.jpg')
    elif label_num == 3:  # PENCIL_DRAWING
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/mediainterior/black_wall.jpg')
    elif label_num == 4:  # IMPRESSIONISM
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/pastel_wall.jpg')
    elif label_num == 5:  # ABSTRACT
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/primary_wall.jpg')
    elif label_num == 6:  # POP_ART
        im1 = PIL.Image.open('C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/interior/primary_wall.jpg')

    image_resized = image.resize((240,int(240/image.size[0]*image.size[1])))
    # image_resized.save('./image_resized.jpg', quality=95) #output1
    back_im = im1.copy() # background
    back_im.paste(image_resized, (380, 400)) # image_resized 된거를 back_im에 붙여넣는다. (380, 400) 은 좌표값

    img_path = 'C:/Users/SeungMin/PycharmProjects/YeZakWeb-main_test/media/merge_interior/result_' + rand_str + '.jpg'
    back_im.save(img_path) #output2

    return image_resized, img_path




















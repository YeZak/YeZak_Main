from CLIP_func import mktag
from CLIP_model import CLIP_tag
import skimage.io as io

image = io.imread(
    "../clip_test_image/modern_impressionism35.jpg")
io.imshow(image)
io.show()

tag = CLIP_tag(image, Is_path = False)

print(tag)

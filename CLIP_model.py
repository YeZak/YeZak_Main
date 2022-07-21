
import clip
import os
from torch import nn
import numpy as np
import torch
import torch.nn.functional as nnf
import sys
from typing import Tuple, List, Union, Optional
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
from tqdm import tqdm, trange
#from google.colab import files
import skimage.io as io
import PIL.Image
from pathlib import Path
#from IPython.display import Image

#from mldemo.settings import BASE_DIR
from CLIP_func import ClipCaptionModel, generate_beam, generate2

BASE_DIR = Path(__file__).resolve().parent.parent


N = type(None)
V = np.array
ARRAY = np.ndarray
ARRAYS = Union[Tuple[ARRAY, ...], List[ARRAY]]
VS = Union[Tuple[V, ...], List[V]]
VN = Union[V, N]
VNS = Union[VS, N]
T = torch.Tensor
TS = Union[Tuple[T, ...], List[T]]
TN = Optional[T]
TNS = Union[Tuple[TN, ...], List[TN]]
TSN = Optional[TS]
TA = Union[T, ARRAY]

D = torch.device
CPU = torch.device('cpu')


if torch.cuda.is_available():
    device = "cuda"

    print(torch.cuda.is_available())

else:
    device = "cpu"    #colab GPU사용량 초과해서 cpu사용 -> false출력

print("Device = ", device)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

clip_model, preprocess = clip.load("ViT-B/32", device=device, jit=False)
#다운 안되면 pip3 install clip-by-openai 설치하기!

#@title Load model weights

prefix_length = 10

model = ClipCaptionModel(prefix_length)

path= os.path.join(BASE_DIR, "model_weights.pt")

#몇몇 인자는 일치 않을 수 있으니 strict = False 추가
model.load_state_dict(torch.load(path, map_location=CPU), strict = False)

model = model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# os.environ['KMP_DUPLICATE_LIB_OK']='True'

#@title Upload Image

image = io.imread("../input.jpg")
io.imshow(image)
io.show()

pil_image = PIL.Image.fromarray(image)

# #@title Inference

use_beam_search = False #@param {type:"boolean"}

image = preprocess(pil_image).unsqueeze(0).to(device)

with torch.no_grad():
    # if type(model) is ClipCaptionE2E:
    #     prefix_embed = model.forward_image(image)
    # else:
    prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
    #prefix = clip_model.encode_image(image)

    print(prefix.shape)

    prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)

if use_beam_search:

    generated_text_prefix = generate_beam(model, tokenizer, embed=prefix_embed)[0]
else:

    generated_text_prefix = generate2(model, tokenizer, embed=prefix_embed)

print('\n')
print(generated_text_prefix)






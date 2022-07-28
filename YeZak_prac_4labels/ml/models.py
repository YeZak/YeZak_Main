import os
import pandas

import torch
from torch import nn
from torchvision.models import resnet18

from mldemo.settings import BASE_DIR

DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "model.pt")

def get_files_count(folder_path):
  dirListing = os.listdir(folder_path)
  return len(dirListing)

datapath_1 = "./YeZak_Dataset_2/ORIE"
datapath_2 = "./YeZak_Dataset_2/REAL"
datapath_3 = "./YeZak_Dataset_2/ANIM"
datapath_4 = "./YeZak_Dataset_2/PENC"
datapath_5 = "./YeZak_Dataset_2/IMPR"
datapath_6 = "./YeZak_Dataset_2/ABST"
datapath_7 = "./YeZak_Dataset_2/POPA"

weight_1 = get_files_count(datapath_1)
weight_2 = get_files_count(datapath_2)
weight_3 = get_files_count(datapath_3)
weight_4 = get_files_count(datapath_4)
weight_5 = get_files_count(datapath_5)
weight_6 = get_files_count(datapath_6)
weight_7 = get_files_count(datapath_7)

arts_num = {'name' : ['동양화', '사실주의', '애니메이션', '연필초상화', '인상주의','추상화', '팝아트'],
               'num' : [weight_1, weight_2, weight_3, weight_4, weight_5, weight_6, weight_7]}

arts = pandas.DataFrame(arts_num)

arts['class_weight'] = arts.num.sum() / (arts.shape[0] * arts.num)

arts_weights = arts['class_weight'].to_dict()

def art_classifier(arts_weights):
    model = resnet18(arts_weights)
    model.fc = nn.Linear(512 * 1, 4)
    return model


def load_default_model(path=DEFAULT_MODEL_PATH):
    model = resnet18()
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model

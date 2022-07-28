import os
import pandas

import torch
from torch import nn
from torchvision.models import resnet18
from yezak.settings import BASE_DIR

DEFAULT_MODEL_PATH = os.path.join(BASE_DIR, "model.pt")


def art_classifier():
    model = resnet18(True)
    model.fc = nn.Linear(512 * 1, 7)
    return model


def load_default_model(path=DEFAULT_MODEL_PATH):
    model = art_classifier()
    model.load_state_dict(torch.load(path, map_location="cpu"))
    model.eval()
    return model


def label_str(prediction_index):

    if (prediction_index == 0):
        label_name = "Orientalism"
    elif (prediction_index == 1):
        label_name = "Realistm"
    elif (prediction_index == 2):
        label_name = "Animation"
    elif (prediction_index == 3):
        label_name = "Pencil"
    elif (prediction_index == 4):
        label_name = "Impressionism"
    elif (prediction_index == 5):
        label_name = "abstract"
    elif (prediction_index == 6):
        label_name = "Pop_art"

    return label_name












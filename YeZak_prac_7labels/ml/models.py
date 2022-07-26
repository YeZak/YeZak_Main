import os
import pandas

import torch
from torch import nn
from torchvision.models import resnet18
from mldemo.settings import BASE_DIR

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

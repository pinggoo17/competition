# 모델을 다시 한번 정의하고, 저장된 모델을 불러옵니다.
import os
from os import listdir
import numpy as np
import torch
import torch.nn as nn
from torchvision.transforms import Compose, CenterCrop, ToTensor, Resize
from PIL import Image

data = np.load("submission.npy", allow_pickle=True)

for i, img in enumerate(data):
    image = Image.fromarray(img)
    print(img.shape)
    image.save(f'{i+1:04}.png', 'PNG')

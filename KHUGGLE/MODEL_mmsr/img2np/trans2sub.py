# 모델을 다시 한번 정의하고, 저장된 모델을 불러옵니다.
import os
from os import listdir
import numpy as np
import torch
import torch.nn as nn
from torchvision.transforms import Compose, CenterCrop, ToTensor, Resize
from PIL import Image

# 추론용 이미지(즉, 손상된 경희대 이미지)를 불러오고, 번호 순서대로 정렬합니다.
# infer_dataset = './image_samples/church_colorization'
infer_dataset = './test_set'
infer_dataset_images = listdir(infer_dataset)
infer_dataset_images.sort()
# infer_dataset_images.sort(key=lambda x: int(x.split('_')[1]))

resize_array = [[580, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [588, 1000],
                [664, 1000],
                [796, 1200],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [536, 1200],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000],
                [664, 1000]]

div = 1

print("infer_dataset: ", infer_dataset_images)

np_list = []

for file, size in zip(infer_dataset_images, resize_array):

    # if (file.endswith('down.png') or file.endswith('orig.png')):
    #     continue

    # if (file.endswith('down.png')):
    #     continue

    print(file)

    out_np = np.asarray(Image.open(infer_dataset+'/'+file))

    print(out_np.shape)
    out_np = Resize((int(size[0]/div), int(size[1]/div))
                    )(Image.open(infer_dataset+'/'+file))
    out_np = np.asarray(out_np)
    print(out_np.shape)

    image = Image.fromarray(out_np)
    os.makedirs(f'./tr{infer_dataset[1:]}', exist_ok=True)
    image.save(f'./tr{infer_dataset[1:]}/{file}', format='png')
    np_list.append(out_np)

# numpy array로 구성된 리스트를 numpy array 형태로 변환합니다.
np_submission_array = np.array(np_list)

# 'submission.npy' 형태로 최종 제출 파일을 정의합니다.
np.save('./submission', np_submission_array)

print('Submission file is complete. Good luck!')

# competition
submission code for competition


# KHUGGLE (2022/12/08, 4th)
- Image Super-resolution task
- Datasets: Low Resolution School images

## 1. Real_HAT_GAN_SRx4
We used <strong>Real_HAT_GAN_SRx4</strong> pretrained models.

You can downlaod Real_HAT_GAN_SRx4.pth [here](https://github.com/XPixelGroup/HAT) <br/>

After putting images and pre-trained models in the folder, you can try this model with following command.

`python hat/test.py -opt options/test/Real_HAT_GAN_SRx4.yml`

please refer to detail [here](https://github.com/XPixelGroup/HAT).

## 2. MMSR_SRResNet
We used <strong>MMSR_SRResNet</strong> pretrained models.

You can downlaod mmsr_SRResNet_pretrain.pth.pth [here](https://github.com/XPixelGroup/RankSRGAN) <br/>

After putting images and pre-trained models in the folder, you can try this model with following command.

`!python test.py -opt options/test/test_RankSRGAN.yml`

please refer to detail [here](https://github.com/XPixelGroup/RankSRGAN).

from PIL import Image
import numpy as np

print(np.asarray(Image.open('./0000.png')).shape)

import os
os.chdir(r'C:\Users\DK0626\Desktop\Python\Data')

from PIL import Image
ii = Image.open('Cat.jpg')
from scipy import misc
f = misc.face()
import matplotlib.pyplot as plt
plt.imshow(ii)
plt.show()


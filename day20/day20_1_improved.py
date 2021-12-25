from day20_data2 import *
import numpy as np
from scipy.ndimage import convolve

convolveMatrix = np.array(
    [
        [ 1,2,4 ],
        [ 8,16,32  ],
        [64,128,256  ]
    ]
)
buffer=60
imgArray = np.array(img)
w,h = imgArray.shape
bufferedImg = np.zeros((w+2*buffer,h+2*buffer))
bufferedImg[buffer:-buffer,buffer:-buffer] = imgArray
times = 2
finalImg = bufferedImg

usedCodex = np.array(codex)

for i in range(times):
    tmp = convolve(finalImg,convolveMatrix)
    finalImg = usedCodex[tmp.astype(int)]
print(np.sum(finalImg))
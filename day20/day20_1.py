from day20_data import *
import numpy as np
from scipy.ndimage import convolve

convolveMatrix = np.array(
    [
        [ 1,2,4 ],
        [ 8,16,32  ],
        [64,128,256  ]
    ]
)
buffer=50
imgArray = np.array(img)
w,h = imgArray.shape
bufferedImg = np.zeros((w+2*buffer,h+2*buffer))
bufferedImg[buffer:-buffer,buffer:-buffer] = imgArray
times = 50
finalImg = bufferedImg
resp = [['#' if col else '.' for col in row] for row in finalImg.astype(int)]

for i in range(times):
    print(i)
    tmp = convolve(finalImg,convolveMatrix)
    tw,th = tmp.shape
    for i in range(tw):
        for j in range(th):
            val = int(tmp[i,j])
            tmp[i,j] = codex[val]
    finalImg = tmp
print(np.sum(finalImg))
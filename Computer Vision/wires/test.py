import numpy as np
import matplotlib.pyplot as plt

from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label

mask_rec = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
)

# arr = np.array([[0, 0, 0, 0, 1, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0]])

arr1 = np.array([[0, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 1, 1],
                 [1, 1, 1, 0, 0, 0, 0]])
arr2 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

print(label(binary_erosion(arr1, mask_rec)))
#
# indices = np.argwhere(arr == 1)
# for index in indices:
#     arr[index[0], index[1] + 1] = 1
#     arr[index[0], index[1] + 2] = 1
#     arr[index[0] + 1, index[1]] = 1
#     arr[index[0] + 1, index[1] + 1] = 1
#     arr[index[0] + 1, index[1] + 2] = 1
# print(arr)

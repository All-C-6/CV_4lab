# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:37:14 2021

@author: ilyan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology as mpl

#создание масок
mask_arr = np.array([[[1,1,1,1], 
                      [1,1,1,1],
                      [1,1,0,0],
                      [1,1,0,0],
                      [1,1,1,1],
                      [1,1,1,1]], 
                     
                     [[1,1,1,1],
                      [1,1,1,1],
                      [0,0,1,1],
                      [0,0,1,1],
                      [1,1,1,1],
                      [1,1,1,1]], 
                     
                     [[1,1,0,0,1,1],
                      [1,1,0,0,1,1],
                      [1,1,1,1,1,1],
                      [1,1,1,1,1,1]], 
                     
                     [[1,1,1,1,1,1],
                      [1,1,1,1,1,1],
                      [1,1,0,0,1,1],
                      [1,1,0,0,1,1]],
                     
                     [[1,1,1,1,1,1],
                      [1,1,1,1,1,1],
                      [1,1,1,1,1,1],
                      [1,1,1,1,1,1]]], dtype = object)

#подготовка к обработке данных
image = np.load('ps1.npy')
objects = [0, 0, 0, 0, 0, 0]

#применение созданных масок
for i in range (len(mask_arr)):
    #пополнение числа найденных объектов
    objects[i] += np.sum(mpl.binary_hit_or_miss(image, mask_arr[i]))

#вывод
for i in range(len(objects) - 1):
    print("Количество найденных объектов %.i типа: %.i" % (i+1, objects[i]))

print("всего объектов: ", np.sum(objects))
plt.figure()
plt.imshow(image, cmap="gray")
plt.show()
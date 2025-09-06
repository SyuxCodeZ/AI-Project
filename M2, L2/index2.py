import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Space Logo.webp')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h, w) = image.shape[:2]

center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype = "uint8")*50
brighter = cv2.add(image, brightness_matrix)
brighter_RGB = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_RGB)
plt.title("Brighter_Image")
plt.show()
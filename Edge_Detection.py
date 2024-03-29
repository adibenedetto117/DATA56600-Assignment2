# -*- coding: utf-8 -*-
"""

@author: AnthonyDiBenedetto
"""

import numpy as np
import matplotlib.pyplot as plt

# define the vertical filter
vertical_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

# define the horizontal filter
horizontal_filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

# read in the bridge image
img = plt.imread('IMG_0329.jpg')

# get the dimensions of the image
n, m, d = img.shape

# initialize the edges image
edges_img = img.copy()

# loop over all pixels in the image
for row in range(3, n - 2):
    for col in range(3, m - 2):
        # create little local 3x3 box
        local_pixels = img[row - 1:row + 2, col - 1:col + 2, 0]

        # apply the vertical filter
        vertical_transformed_pixels = vertical_filter * local_pixels
        # remap the vertical score
        vertical_score = vertical_transformed_pixels.sum() / 4

        # apply the horizontal filter
        horizontal_transformed_pixels = horizontal_filter * local_pixels
        # remap the horizontal score
        horizontal_score = horizontal_transformed_pixels.sum() / 4

        # combine the horizontal and vertical scores into a total edge score
        edge_score = (vertical_score ** 2 + horizontal_score ** 2) ** .5

        # insert this edge score into the edges image
        edges_img[row, col] = [edge_score] * 3

# remap the values in the 0-1 range in case they went out of bounds
edges_img = edges_img / edges_img.max()

# Set up a subplot configuration: 1 row, 2 columns
plt.figure(figsize=(20, 10))  # Adjust the figure size as needed

# First subplot for the original image
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.imshow(img)
plt.axis('off')  # Turn off axis numbers and ticks

# Second subplot for the edges image
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.imshow(edges_img)
plt.axis('off')

# Display the figure
plt.show()
import cv2, sys
import numpy as np

from matplotlib import pyplot as plt

# Prompt for bounds
lower_bound = int(input("What should be the lower bound for the 2G_RBi? (default: 25)") or "25")
higher_bound = int(input("What should be the higher bound for the 2G_RBi? (default: 175)") or "175")

# Use 2nd argument as filename
img = cv2.imread(sys.argv[1])

# Create gray image from colour image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Split RGB-channels
b,g,r = cv2.split(img)

# Calculate VI
twoG_RBi = 2 * g - (r + b)

# Create the mask
mask = cv2.inRange(twoG_RBi, lower_bound, higher_bound)
 
# Create the inverted mask
mask_inv = cv2.bitwise_not(mask)

masked_data = cv2.bitwise_and(img, img, mask=mask_inv)
rev_masked_data = cv2.bitwise_and(img, img, mask=mask)

# Set gray value (i.e. 100)
masked_data[mask_inv == 0] = (0, 255, 0)
rev_masked_data[mask == 0] = (0, 255, 0)

titles = ['Original Image','2G_RBi','Mask','Inv. Mask']
images = [img, twoG_RBi, masked_data, rev_masked_data]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.suptitle("Vegetation Index")

plt.show()
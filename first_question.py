import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from os import path

# Request user input for the image name
print("Enter the full path to the image (e.g., /path/to/image.jpg): ")
image_path = input()

# Check if the image exists
if not path.exists(image_path):
    print("Image Not Found!")
    exit()

# Load the image
img = cv.imread(image_path)

# Split the image into its color channels
b, g, r = cv.split(img)

# Display the original image
cv.imshow("Original Image", img)

# Plot histograms for each color channel
plt.hist(b.ravel(), 256, [0, 256], color='blue', alpha=0.5, label='Blue Channel')
plt.hist(g.ravel(), 256, [0, 256], color='green', alpha=0.5, label='Green Channel')
plt.hist(r.ravel(), 256, [0, 256], color='red', alpha=0.5, label='Red Channel')

# Calculate and plot overall histogram
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='black', label='Overall Histogram')

# Add title and labels to the histogram
plt.title("Color Channel Histograms")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

# Show the histogram
plt.show()

# Wait for a key press to close the image window
cv.waitKey(0)

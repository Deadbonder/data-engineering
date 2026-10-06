import cv2

image = cv2.imread('matplotlib_practice/wine_plots.png')
print(type(image))   #an image is just a numpy array
print(image.shape)   #(height, width, channels) - channels are B, G, R

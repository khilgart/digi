import numpy as np
import PIL as pl
import matplotlib.pyplot as plt
#from pkg_resources import invalid_marker

test = pl.Image.open("road.jpg")        #open image and turn to array
test_arr = np.array(test)
gray_arr = np.array(test)

#greyscale algo
for x in range(len(test_arr)):
    for y in range(len(test_arr[x])):                   #nested for loops cycle through every pixel in test image
        red = test_arr[x, y, 2]                         #gets red hue from pixel
        green = test_arr[x, y, 1]                       #get green hue from pixel
        blue = test_arr[x, y, 0]                        #gets blue hue from pixel
        gray = red*0.2126 + green*0.7152 + blue*0.0722  #converts pixel to greyscale value using ITU-R Rec. BT.709
        gray_arr[x, y] = gray                           #inserts grayscale pixel value into image array
test2 = pl.Image.fromarray(gray_arr)                    #converts image array w/ new gray values back into picture

"""fig = plt.figure()                                  
plt.subplot(1, 2, 1)        #shows the original image
plt.imshow(test)
plt.title("Original")
plt.axis('off')
plt.subplot(1, 2, 2)        #shows new image
plt.imshow(test2)
plt.axis('off')
plt.title("Grayscale")"""

#image blur w/ averaging kernel 
gray2 = np.array(test2)
for x in range(1, len(gray2) - 1): #loops through all pixels in image except for the outer ones
    for y in range(1, len(gray2[x]) - 1):
        ksum = np.sum(gray_arr[x-1:x+2, y-1:y+2, 1]) / 9.0     #taking average of kernel to keep image same brightness 
        gray2[x, y] = ksum
test4 = pl.Image.fromarray(gray2) #above loop takes the average of the pixel and the pixels above, below, and sides of it

fig4 = plt.figure()                                  
plt.subplot(2, 1, 1)        #shows the original image
plt.imshow(test2)
plt.title("Grayed")
plt.axis('off')
plt.subplot(2, 1, 2)        #shows new image
plt.imshow(test4)
plt.axis('off')
plt.title("Smoothed")

plt.show()
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.jpg') #Get the image

R, G, B = img[:,:,0], img[:,:,1], img[:,:,2] #Split RGB channels
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B #Convert all channels to grayscale.
plt.imshow(imgGray, cmap='gray') #Show the image.
plt.show()


#https://www.delftstack.com/howto/python/convert-image-to-grayscale-python/

# https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
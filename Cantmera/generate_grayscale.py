from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy

#image = "ct34"
image_ext = ".jpg"
image_list = ["ct1","ct3","ct4","ct5","ct6","ct7","ct8","ct9","ct10","ct11","ct12","ct13",
			"ct14","ct15","ct16","ct17","ct18","ct19","ct20","ct21","ct22","ct23","ct24","ct25","ct26",
			"ct27","ct28","ct29","ct30","ct31","ct32","ct33","ct34", "ct35"]
methods = ["BT601", "BT709"]
method = "BT601"

for current_image in image_list:
	# img = mpimg.imread(image + image_ext) #Get the image
	img = mpimg.imread(current_image + image_ext)
	for method in methods:
		R, G, B = img[:,:,0], img[:,:,1], img[:,:,2] #Split RGB channels
		
		if method == "BT601":
			imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B #Convert all channels to grayscale.
		elif method == "BT709":
			imgGray = 0.2126 * R + 0.7152 * G + 0.0722 * B
		elif method == "Decomposition_MAX":
			imgGray = numpy.copy(img)
			for ix in range(len(img)):
				for iy in range(len(img[ix])):
					val = max(img[ix, iy, 0], img[ix, iy, 1], img[ix, iy, 2]) #Determine max value of channels.
					imgGray[ix, iy, 0] = val #Set all channels to the same value.
					imgGray[ix, iy, 1] = val
					imgGray[ix, iy, 2] = val
			
		elif method == "Decomposition_MIN":
			imgGray = numpy.copy(img)
			for ix in range(len(img)):
				for iy in range(len(img[ix])):
					val = min(img[ix, iy, 0], img[ix, iy, 1], img[ix, iy, 2]) #Determine min value of channels.
					imgGray[ix, iy, 0] = val #Set all channels to the same value.
					imgGray[ix, iy, 1] = val
					imgGray[ix, iy, 2] = val

		plt.title(current_image + "_" + method + image_ext)
		fig = plt.gcf()
		fig.canvas.set_window_title(current_image + "_" + method + image_ext)
		mpimg.imsave(current_image + "_" + method + image_ext, imgGray, cmap='gray')
		# plt.imshow(imgGray, cmap='gray') #Show the image.
		# plt.show()

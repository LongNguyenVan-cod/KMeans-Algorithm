import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

# Read file image
image = plt.imread('a.jpg')

# Create width, height of image
width = image.shape[0]
height = image.shape[1]

# Reshape mensional of image
image = image.reshape(width*height, 4)

# Use algorithm
kmeans = KMeans(n_clusters=4 ).fit(image)
labels = kmeans.predict(image)
clusters = kmeans.cluster_centers_
# print(labels)
# print(clusters)

# Craete image_2 like mensional image after reshape
image_2 = numpy.zeros((width,height,4), dtype=numpy.float32)  #float32, uint8

index = 0
for i in range(width):
	for j in range(height):
		labels_of_index = labels[index]
		image_2[i][j] = clusters[labels_of_index]
		index +=1

plt.imshow(image_2)
plt.show()

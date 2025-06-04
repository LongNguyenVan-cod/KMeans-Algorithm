import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

# Read file image
image = plt.imread('a.jpg')

# Create width, height of image
width = image.shape[0]
height = image.shape[1]

print(image.shape)

# Reshape mensional of image
image = image.reshape(width*height, 3 )
print(image.shape)

# Use algorithm
kmeans = KMeans(n_clusters=4 ).fit(image)

# Take labels and clusters
labels = kmeans.predict(image)
clusters = kmeans.cluster_centers_
print(labels)
print(clusters)

# Craete image_2 like mensional image after reshape
# image_2 = numpy.zeros_like(image)
image_2 = numpy.zeros((width,height,3 ), dtype=numpy.uint8)  #float32, uint8

# for i in range(len(image_2)):
# 	image_2[i] = clusters[labels[i]]

index = 0
for i in range(width):
	for j in range(height):
		labels_of_index = labels[index]
		image_2[i][j] = clusters[labels_of_index]
		index +=1

# image_2 = image_2.reshape(width,height,3)

plt.imshow(image_2)
plt.show()
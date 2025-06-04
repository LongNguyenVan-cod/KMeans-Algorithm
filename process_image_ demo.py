import matplotlib.pyplot as plt 
import numpy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score 
import math

def distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2+(p1[3]-p2[3])**2)

image = plt.imread('image.jpg')
print(image.shape) 

width = image.shape[0]
height = image.shape[1]

# 3 the hien la anh mau RGB
image = image.reshape((width*height), 4 )
print(image.shape)
print(image)


kmax = [2,3,4,5,6,7,8,9,10]
dis_tance = []
# sil_score = []
# image_2 = image.copy()
for k in kmax:

	kmeans = KMeans(n_clusters=k).fit(image)

	labels = kmeans.predict(image)
	clusters = kmeans.cluster_centers_
	# print(labels)
	# print(clusters)

	# print(image_2) 

	# sil_score.append(silhouette_score(image, label, metric='euclidean'))

	dis = 0
	for i in range(len(image)):
		image_predict = clusters[labels[i]]
		dis += distance(image_predict, image[i])

	dis_tance.append(dis)

print(dis_tance)
# print(sil_score)

figure, axis = plt.subplots()

plt.plot(kmax, dis_tance, marker='o')

plt.xlabel('k')
plt.ylabel('Eucliden distance')
# axis.set_ylim(0.5*1e7, 2.5*1e7)
# plt.plot(kmax, sil_score)
plt.show()

# image_2 = numpy.zeros((width,height,3), dtype=numpy.uint8)

# index = 0
# for i in range(width):
# 	for j in range(height):
# 		image_2[i][j] = clusters[labels[index]]
# 		index += 1

# plt.imshow(image_2)
# plt.show()

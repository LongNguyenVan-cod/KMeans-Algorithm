import matplotlib.pyplot as plt 
import numpy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score 
import math

def distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2+(p1[3]-p2[3])**2)

image = plt.imread('image.jpg')

width = image.shape[0]
height = image.shape[1]

image = image.reshape((width*height), 4 )
print(image.shape)
print(image)

# List values k
kmax = [2,3,4,5,6,7,8,9,10]
dis_tance = []

for k in kmax:

	kmeans = KMeans(n_clusters=k).fit(image)

	labels = kmeans.predict(image)
	clusters = kmeans.cluster_centers_

	dis = 0
	for i in range(len(image)):
		image_predict = clusters[labels[i]]
		dis += distance(image_predict, image[i])

	dis_tance.append(dis)

print(dis_tance)

figure, axis = plt.subplots()
plt.plot(kmax, dis_tance, marker='o')

plt.xlabel('k')
plt.ylabel('Eucliden distance')
axis.set_ylim(0.5*1e7, 2.5*1e7)
plt.show()



# plt.imshow(image_2)
# plt.show()

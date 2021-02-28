import numpy as np
import copy
import matplotlib.pyplot as plt

original = [[1,20], [20,3], [8,9]]
scaleFactor = 2
scaled = copy.deepcopy(original)
for i in range(len(scaled[0])):
    scaled[0][i]=scaled[0][i]*scaleFactor
    scaled[1][i]=scaled[1][i]*scaleFactor
# X = np.array(original)
X = np.array(original + scaled)

# X = np.array([[1,1], [2,2.5], [3, 1], [8, 7.5], [7, 9], [9, 9]])
r = 'red'
b = 'blue'
Y = []
Y += len(original)*[r]
Y += len(original)*[b]

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)

t2 = plt.Polygon(X[3:6,:], color=Y[3])
plt.gca().add_patch(t2)

plt.show()
# plt.figure()
# plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

# t1 = plt.Polygon(X[:3,:], color=Y[0])
# plt.gca().add_patch(t1)
# print(scaled)

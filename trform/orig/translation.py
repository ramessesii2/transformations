import numpy as np
import copy
import matplotlib.pyplot as plt
def matrix_mul(matrix1,matrix2):
	new_matrix = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(matrix1)):
	    for j in range(len(matrix2[0])):
	        for k in range(len(matrix2)):
	            new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
	return np.around(new_matrix,decimals=2)
Tx = 4
Ty = 5
TranMatrix = np.zeros((3,3))
TranMatrix[0][0]=1
TranMatrix[0][2]=Tx
TranMatrix[1][1]=1
TranMatrix[1][2]=Ty
TranMatrix[2][2]=1

original = [[1,2], [20,10], [-2,4]]
translated=matrix_mul(TranMatrix, original)
l = []
for i in range(len(translated)):
	l.append([])
	for j in range(len(translated[0])-1):
		l[i].append(translated[i][j])
print(original)
print(l)
X = np.array(original + l)

# X = np.array([[1,1], [2,2.5], [3, 1], [8, 7.5], [7, 9], [9, 9]])
r = 'red'
b = 'blue'
Y = []
Y += len(original)*[r]
Y += len(original)*[b]

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

t1 = plt.Polygon(X[:len(original),:], color=Y[0])
plt.gca().add_patch(t1)

t2 = plt.Polygon(X[len(original):2*len(l),:], color=Y[3])
plt.gca().add_patch(t2)

plt.show()
# print(translated)

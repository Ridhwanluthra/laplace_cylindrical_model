# Simple Numerical Laplace Equation Solution using Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
lenX = lenY = 20 #we set it rectangular
delta = 1
mid = lenX // 2

# Boundary condition
Ttop = 0
# Tbottom = 0
Tleft = 0
Tright = 0

# Initial guess of interior grid
Tguess = 0

# Set colour interpolation and colour map
colorinterpolation = 50
colourMap = plt.cm.jet #you can try: colourMap = plt.cm.coolwarm

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX, lenY))
T.fill(Tguess)

# Set Boundary condition
T[(lenY-1):, :] = Ttop
# T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft

for i in range(lenY):
	T[0][i] = (1-(abs(i-mid)**2/mid**2))
	# print(T[0][i])
	print(abs(i-mid))

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
        	# if T[i][j] != 0:
        	# 	T[i, j] = (1 - (T[i - 1][j] / T[i][j]) + (T[i + 1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])) / 4
        	# else:
        	# 	T[i, j] = 0

            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])


print("Iteration finished")

# Configure the contour
plt.title("Contour of Temperature")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")
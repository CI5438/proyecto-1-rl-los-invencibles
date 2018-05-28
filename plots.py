"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco
	Fabiola Martinez 1310838
"""

import math
import sys
import random
import matplotlib.pyplot as plt
from project_1 import *

def plotScatter(x,y,xlabel,ylabel,title):
	plt.scatter(x_1, y_1)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

# 2.1) ------------------------------------------------------------------------

filename1 = "x01.txt"
read_dataset(filename1)

# Without normalized the data -------------------------------------------------

# Question a) -----------------------------------------------------------------

# Question b) -----------------------------------------------------------------

# Normalized data -------------------------------------------------------------

# Question a) -----------------------------------------------------------------

# Question b) -----------------------------------------------------------------

norm()
theta_1 = gradient_descent(0.001)
x_1 = []
y_1 = []

for i in range(len(x)):
	x_1.append(x[i][1])
	y_1.append(theta_1[0] + theta_1[1]*x[i][1])

plotScatter(x_1,y_1,"Brain Weight", "Body Weight", "Exercise 2.1.b")

# 2.2) ------------------------------------------------------------------------
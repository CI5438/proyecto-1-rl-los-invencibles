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

theta = [0,0]
features = []
x = []
y = []

def read_dataset(filename):
	dataset = open(filename, "r")

	i=0

	for line in dataset:
		word = line.split()
		
		if word[0][0] != "#":
			i+=1
			if i == 1:
				columns = int(word[0])
				# print(columns)
			elif i == 2:
				rows = int(word[0])
				# print(rows)
					
				for j in range(columns):
					line = next(dataset)
					features.append(line.split())
			else:
			 	
			 	x.append(word[1])
				y.append(word[2])

def h(theta, x):
	return theta[0] + theta[1]*x

def j(theta, x, y):
	plus=0
	for i in range (0, len(x)):
		plus += (h(theta, x[i]) - y[i])**2
	return (1/(2*n))*plus

def norm2(x):
	plus=0
	for i in range (0, len(x)):
		plus += x[i]**2
	return math.sqrt(plus)

def sub_vec(a,b):
	c=[]
	for i in range (0,len(a)):
		c[i]=a[i]-b[i]
	return c

def gradient_descent(theta, alpha):
	theta_old=[0,0]
	theta_new=theta
	epsilon=0.001
	while(norm2(sub_vec(th))<epsilon): #condicion de convergencia
		theta_new=sub_vec(theta_old, )

filename = "x01.txt"
read_dataset(filename)

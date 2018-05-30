"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco 1310156
	Fabiola Martinez 1310838

Description: linear regression algorithm.

"""
import math # useful for mathematical operators
import sys
import random  # useful for random function


"""
Description: gets information about dataset.

Parameters:
	@param filename: name of de dataset file.
"""
def read_dataset(filename):
	x = []
	y = []
	features = []
	i=0
	columns=0

	dataset = open(filename, "r")

	for line in dataset:
		word = line.split()
		
		if word[0][0] != "#":
			i+=1
			if i == 1:
				columns = int(word[0])
			
			elif i == 2:
				rows = int(word[0])
					
				for j in range(columns):
					line = next(dataset)
					features.append(line.split())
			else:
				aux=[]
				for j in range(columns-1):
					if j==0:
						aux.append(1)
					else:
						aux.append(float(word[j]))
				x.append(aux)
				y.append(float(word[columns-1]))

	# Dataset
	# for i in range(len(x)):	
	# 	for j in range (1,columns-1):
	# 		print(x[i][j], end=' ')
	# 	print(y[i])
	# print(" ")

	return x, y

"""
Description: normalizes the data.
Parameters:
	@param x: data to normalizes.
"""
def norm(x):
	media=[1]
	varianza=[1]
	
	for i in range(1,len(x[0])):
		aux=0
		for j in range(len(x)):
			aux+=x[j][i]
		media.append(aux/len(x))
	
	for i in range(1,len(x[0])):
		aux=0
		for j in range(len(x)):
			aux+=(x[j][i]-media[i])**2
		varianza.append((aux/(len(x)-1))**(1/2))
	
	for i in range(1,len(x[0])):
		for j in range(len(x)):
			x[j][i]=(x[j][i]-media[i])/varianza[i]

	# Data normalized
	# for i in range(len(x)):	
	# 	#print(columns)
	# 	for j in range (len(x[i])):
	# 		print(x[i][j], end=' ')
	# 	print(y[i])
	# print(" ")

	return x

"""
Description: calculates the derived cost function..

Parameters:
	@param theta: array with theta values.
	@param x: values of dataset variable.
"""
def h(theta, x):
	#print (float(theta[1])*float(x[1]))
	aux=0
	for i in range(len(theta)):
		aux+=theta[i]*x[i]
	return aux

"""
Description: calculates the cost function.

Parameters:
	@param theta: array with theta values.
	@param x: values of dataset variable.
	@param y: values of dataset variable.
"""
def jfunc(theta,x,y):
	plus=0
	for i in range(0, len(x)):
		plus += (h(theta, x[i]) - y[i])**2
	return (1/(2*len(x)))*plus

"""
Description: calculates the norm of a vector.

Parameters:
	@param x: values of dataset variable.
"""
def norm2(x):
	plus=0
	for i in range (0, len(x)):
		plus += x[i]**2
	return math.sqrt(plus)

"""
Description: subtracts two vectors.

Parameters:
	@param a: a vector.
	@param b: a vector.
"""
def sub_vec(a,b):
	c=[]
	for i in range (0,len(a)):
		c.append(a[i]-b[i])
	return c

"""
Description: gradient descent algorithm.

Parameters:
	@param alpha: learning rate.
"""
def gradient_descent(alpha,x,y,max_it):
	theta_old=[]
	theta_new=[]
	jota=[]
	epsilon=10**-2
	k=0
	
	for i in range(len(x[0])):
		theta_old.append(random.random()*100)
		theta_new.append(0)

	jota.append(jfunc(theta_new,x,y))
	while(norm2(sub_vec(theta_new,theta_old))>epsilon and k<max_it): #condicion de convergencia
		
		for i in range(len(x[0])):
			theta_old[i] = theta_new[i]
			
		for i in range (0, len(theta_old)):
			plus=0
			
			for j in range (0, len(x)):
				plus+=(h(theta_old, x[j])-y[j])*x[j][i]
			theta_new[i]=theta_old[i]-(alpha*(1/len(x))*plus)
		jota.append(jfunc(theta_new,x,y))

		print(k)
		
		k+=1
	
	#Theta values and iterations
	for i in range(len(theta_new)):
		print("Theta ", i, ": ", theta_new[i])
	print("k: ", k)

	return theta_new, jota

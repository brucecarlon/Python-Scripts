'''
This program estimates pi by considering a unit circle enclosed a square.
In order to estimate pi, the hit and miss method was employed, we consider
a 2 x 2 square piece of paper with an inscribed circle of radius 1, we then simulate throwing
darts at the sqaure and we have the following relations:
    
    (number of dots inside circle)/(total number of dots) = (area of circle)/(area of square)

13 May 2019
Bruce Mvubele

'''



import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random



# Create x and y variable for the dots consisting of random numbers
# this will be the simulation of dart throwing
y = random.uniform(-1,1,150)
x = random.uniform(-1,1,150)




#create Circle
r = 1 # radius of circle
thetha = np.arange(0,2*np.pi,.01) # angular variable
circle_x = r*np.cos(thetha)
circle_y = r*np.sin(thetha)

# Plot the simulation
plt.plot(circle_x,circle_y)
plt.scatter(x,y)
plt.show()

# number of dots inside circle
inside = 0

i = 0
q = 0
darts = 150

#Finding number of dots in circle       
for i in range(0,darts):
    x = x**2
    y = y**2
    if np.sqrt(np.any(x) + np.any(y)) < 1 :
        inside = inside + 1
        
        
print(f'Number of dots inside the circle is {inside} out of a total of {darts}')
pi = (float(inside)/150) *4
print(f'pi \u2248 {pi}')
print(f'error = {abs(np.pi - pi)}')


# for statistical purposes we can do the simulation 5 times and take the 
# average as the best estimate
# #Extracted pi estimates
# pi_est = [3.546,3.466,3.573,3.520,3.530]
# print('pi avge', np.sum(pi_est)/5)
# mean = np.mean(pi_est)
# var = np.var(pi_est)
# std = np.sqrt(np.var(pi_est))

# print('mean =', mean)
# print('standard deviation =', std)


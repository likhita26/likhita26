from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

#if using termux
import subprocess
import shlex
#end if

# Create the figure
fig = plt.figure()
point1  = np.array([1, 1, 0])
normal = np.array([1,-6, 2])
point2 = np.array([1, 2, 3])
point3 = np.array([3,1,1])
# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point1.dot(normal)
# create x,y
xx, yy = np.meshgrid(range(10), range(10))
# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z, alpha=0.6)
#defining lines : x(k) = A + k*l
A1 = np.array([1,1,0]).reshape((3,1))
l1 = np.array([2,1,4]).reshape((3,1))
A2 =  np.array([1,1,0]).reshape((3,1))
l2 = np.array([0,1,3]).reshape((3,1))
#defining point of intersection
P = np.array([1,1,0])
#generating points in line 
l1_p = line_dir_pt(l1,A1)
l2_p = line_dir_pt(l2,A2)
#plotting line
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line L1")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line L2")
#and i would like to plot this point : 
plt3d.scatter(point2[0] , point2[1] , point2[2],  color='green')
plt3d.text(point2[0] * (1 + 0.1), point2[1] * (1 - 0.1),point2[2]*(1) , 'B')
plt3d.scatter(point1[0] , point1[1] , point1[2],  color='red')
plt3d.text(point1[0] * (1 + 0.1), point1[1] * (1 - 0.1) ,point1[2]*(1)  , 'P')
plt3d.scatter(point3[0] , point3[1] , point3[2],  color='blue')
plt3d.text(point3[0] * (1 + 0.1), point3[1] * (1 - 0.1), point3[2]*(1) , 'A')

plt.legend()
plt.show()

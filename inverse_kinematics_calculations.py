import numpy as np
import math
#link lengths of the robotic arm are entered
a1 = 40.0
a2 = 40.0
a3 = 30.0
#the required position of end effector is given as input
#end effector position should be given as coordinates and rotation matrix in 3-D space 
X = float(input('enter the X coordinate of the endeffector - '))
Y = float(input('enter the Y coordinate of the endeffector - '))
Z = float(input('enter the Z coordinate of the end effector - '))
R0_4 = [[[]for i in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        n = int(input('enter element of rotation matrix - '))
        R0_4[i][j] = n
print(R0_4)
#rotation parameters are calculated
f = float(Y/X)
t1 = np.arctan(f)
r = np.sqrt(X**2+Y**2)
print(r)
a = float((math.pow(a3,2)-math.pow(a2,2)-math.pow(r,2))/(-2*a2*r))
print(a)
t2 = np.arccos(a)
b = ((math.pow(r,2)-math.pow(a2,2)-math.pow(a3,2))/(-2*a2*a3))
p = np.arccos(b)
t3 = np.radians(180)-p
R0_3 = [[np.cos(t1+t2+t3),-np.sin(t1+t2+t3),0.0],[0.0,0.0,1.0],[np.sin(t1+t2+t3),
        np.cos(t1+t2+t3),0.0]]
r0_3 = np.linalg.inv(R0_3)
print(r0_3)
#print(R0_4)
r3_4 = np.dot(r0_3,R0_4)
print(r3_4)
t4 = np.arcsin(r0_3[1][0])
print(np.degrees(t4))


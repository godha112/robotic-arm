import numpy as np
import math
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
a1 = 40.0
a2 = 40.0
a3 = 30.0
s1 = 7
s2 = 11
s3 = 13
s4 = 14
gpio.setup(s1,gpio.OUT)
gpio.setup(s2,gpio.OUT)
gpio.setup(s3,gpio.OUT)
gpio.setup(s4,gpio.OUT)
X = float(input('enter the X coordinate of the endeffector - '))
Y = float(input('enter the Y coordinate of the endeffector - '))
Z = float(input('enter the Z coordinate of the end effector - '))
R0_4 = [[[]for i in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        n = int(input('enter element of rotation matrix - '))
        R0_4[i][j] = n
print(R0_4)
#R0_4 = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
#R0_4.astype(float)
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


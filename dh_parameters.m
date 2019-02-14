clc
clear all
n_frames = input('enter the number of frames - ');
n = n_frames-1;
p = input('enter the dh parameter table - ')
t = degtorad(p(:,1))
a = degtorad(p(:,2))
p(:,1) = t
p(:,2) = a
for i=1:n
    H(:,:,i) = [cos(p(i,1)),-sin(p(i,1))*cos(p(i,2)),sin(p(i,1))*sin(p(i,2)),p(i,3)*cos(p(i,1));
        sin(p(i,1)),cos(p(i,1))*cos(p(i,2)),-cos(p(i,1))*sin(p(i,2)),sin(p(i,1))*p(i,3);
        0,sin(p(i,2)),cos(p(i,2)),p(i,4);0,0,0,1]
end
E = 1
for i=1:n
    E = E*H(:,:,i)
end
disp('homogeneous transformation matrix of end effector - ')
disp(E)
disp('x coordinate of the end effector is - ')
disp(E(1,4))
disp('y coordinate of the end effector is - ')
disp(E(2,4))
disp('z coordinate of the end effector is - ')
disp(E(3,4))

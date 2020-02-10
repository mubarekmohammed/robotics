%%The following script calculates the joint angles for 3DOF robot arm. It
%%utilizes the Robotics ToolBox built by Peter Corke.
% before running the program please visit http://www.petercorke.com to
% download robotics toolbox.
% initialize the toolbox on the matlab command line by typing 
% startup_rvc

clc 
clear all

startup_rvc;

%%

%set of arm length values
a1 = 6;
a2 = 6;
a3 = 6;

%generates a set of angles 
theta = linspace(0, 2*pi ,21);
r = 2;
output = zeros(length(theta),1);
x = zeros(21,1);
y = zeros(21,1);
theta1 = zeros(length(theta),1);
theta2 = zeros(length(theta),1);
theta3 = zeros(length(theta),1);
z = zeros(21,1);

%calculates a set of points that form a circle 
for i = 1: 21
    
    x(i) = r*cos(theta(i));
    y(i) = r*sin(theta(i));
   
    %theta(i)
end

%inverse kinematics eqn to calculate set of theta values for the joint
%angles
for i = 1:21
 
  val = y(i)/x(i);
  theta1(i) = atan(val);  
  r1 = sqrt(x(i)^2 + y(i)^2);
  r_2 = z(i) - a1;
  val1 = r_2/r1;
  phi_2 = atan(val1);
  r_3 = sqrt((r1)^2 + (r_2)^2);
  phi_1 = acos(((a3)^2 - (a2)^2 - (r_3)^2)/(-2 * a2 * r_3));
  theta2(i) = phi_2 - phi_1;
  phi_3 = acos(((r_3)^2 - (a2)^2 - (a3)^2)/(-2 * a2 * a3));
  theta3(i) = pi - phi_3;
     
    
end   




%%Utilizes the Robotic Toolbox built by Peter Corke
% Initializes the Link 1, 2 and 3 
L(1) = Link([0 6 0 pi/2 0]);
L(2) = Link([0 0 6 0 0]);
L(3) = Link([0 0 6 0 0]);

three_link = SerialLink(L, 'name', 'robot_arm');



% %%
% t0 = [0.78539816 -2.87542627 4.65680481-pi];
% t1 = [0.89605538 -3.03202815 4.65680481-pi];
% t2 = [0.86217005 -2.73352922 4.65680481-pi];
% t3 = [0.89605538 -3.03202815 4.65680481-pi];
% t4 = [0.78539816 -2.87542627 4.65680481-pi];
% t5 = [0.46364761 -3.03202815 4.65680481-pi];
%%
%set of angles calculated from the inverse kinematics eqn
t_1 = [theta1(1) theta2(1) theta3(1)-pi/2];
t_2 = [theta1(2) theta2(2) theta3(2)-pi/2];
t_3 = [theta1(3) theta2(3) theta3(3)-pi/2];
t_4 = [theta1(4) theta2(4) theta3(4)-pi/2];
t_5 = [theta1(5) theta2(5) theta3(5)-pi/2];
t_6 = [theta1(6) theta2(6) theta3(6)-pi/2];
t_7 = [theta1(7) theta2(7) theta3(7)-pi/2];
t_8 = [theta1(8) theta2(8) theta3(8)-pi/2];
t_9 = [theta1(9) theta2(9) theta3(9)-pi/2];
t_10 = [theta1(10) theta2(10) theta3(10)-pi/2];
t_11 = [theta1(11) theta2(11) theta3(11)-pi/2];
t_12 = [theta1(12) theta2(12) theta3(12)-pi/2];
t_13 = [theta1(13) theta2(13) theta3(13)-pi/2];
t_14 = [theta1(14) theta2(14) theta3(14)-pi/2];
t_15 = [theta1(15) theta2(15) theta3(15)-pi/2];
t_16 = [theta1(16) theta2(16) theta3(16)-pi/2];
t_17 = [theta1(17) theta2(17) theta3(17)-pi/2];
t_18 = [theta1(18) theta2(18) theta3(18)-pi/2];
t_19 = [theta1(19) theta2(19) theta3(19)-pi/2];
t_20 = [theta1(20) theta2(20) theta3(20)-pi/2];
t_21 = [theta1(21) theta2(21) theta3(21)-pi/2];




%%
%calculates the forward kinematics of the robot arm using the Robotics
%Toolbox 
T1 = three_link.fkine(t_1);
T2 = three_link.fkine(t_2);
T3 = three_link.fkine(t_3);
T4 = three_link.fkine(t_4);
T5 = three_link.fkine(t_5);
T6 = three_link.fkine(t_6);
T7 = three_link.fkine(t_7);
T8 = three_link.fkine(t_8);
T9 = three_link.fkine(t_9);
T10 = three_link.fkine(t_10);
T11 = three_link.fkine(t_11);
T12 = three_link.fkine(t_12);
T13 = three_link.fkine(t_13);
T14 = three_link.fkine(t_14);
T15 = three_link.fkine(t_15);
T16 = three_link.fkine(t_16);
T17 = three_link.fkine(t_17);
T18 = three_link.fkine(t_18);
T19 = three_link.fkine(t_19);
T20 = three_link.fkine(t_20);
T21 = three_link.fkine(t_21);

%%

%initializes time array
tim = linspace(0,1,10);

%Generates Joint trajectory of the robot arm.
q = jtraj(t_1,t_2,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_2,t_3,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_3,t_4,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_4,t_5,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_5,t_6,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_6,t_7,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_7,t_8,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_8,t_9,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_9,t_10,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_10,t_11,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_11,t_12,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_12,t_13,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_13,t_14,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_14,t_15,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_15,t_16,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_16,t_17,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_17,t_18,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_18,t_19,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_19,t_20,tim);
three_link.plot(q)
pause(0.05)
q = jtraj(t_20,t_21,tim);
three_link.plot(q)







    


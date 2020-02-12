#calculates the inverse kinematics of 3 DOF robot arm. The value of angles for joint 1 , 2 and 3 are calculated based 
#on a set of points that correspond to a circle in a 3D plane

import numpy as np 
import matplotlib.pyplot as plt
import csv
from numpy import asarray


def main():


    #link lengths 
    #y0_3 = 2
    #x0_3 = 2
    #z0_3 = 0
    a_1 = 6
    a_2 = 6
    a_3 = 6

    #set of x, y and z values that correspond to the shape of a circle 
    #the circle is gonna be on the x,y plane 
    x = [2,
    1.90211303259031,
    1.61803398874990,
    1.17557050458495,
    0.618033988749895,
    1.22464679914735e-16,
    -0.618033988749895,
    -1.17557050458495,
    -1.61803398874989,
    -1.90211303259031,
    -2,
    -1.90211303259031,
    -1.61803398874990,
    -1.17557050458495,
    -0.618033988749895,
    -3.67394039744206e-16,
    0.618033988749895,
    1.17557050458495,
    1.61803398874989,
    1.90211303259031,
    2]
    y = [0,
    0.618033988749895,
    1.17557050458495,
    1.61803398874990,
    1.90211303259031,
    2,
    1.90211303259031,
    1.61803398874990,
    1.17557050458495,
    0.618033988749895,
    2.44929359829471e-16,
    -0.618033988749894,
    -1.17557050458495,
    -1.61803398874989,
    -1.90211303259031,
    -2,
    -1.90211303259031,
    -1.61803398874990,
    -1.17557050458495,
    -0.618033988749895,
    -4.89858719658941e-16]
    z = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #initializing a array of theta values 
    theta_1a = [0 for i in range(21)]
    theta_2a = [0 for i in range(21)]
    theta_3a = [0 for i in range(21)]

    #for loop to calculate the theta values utilizing the inverse kinematics equation derived from the
    # orientation of the 3DOF robot arm 
    for i in range(len(x)):
        theta_1a[i] = np.arctan(y[i]/x[i])
        #theta_1a[i]*=(180/(np.pi))
        r_1 = (np.sqrt((x[i])**2 + (y[i])**2))
        r_2 = z[i] - a_1
        phi_2 = np.arctan(r_2/r_1)
        #print(r_1)
        #print(r_2)
        r_1s = (r_1) ** 2
        r_2s = (r_2) ** 2
        #print(r_1s)
        #print(r_2s)
        r_p = r_1s + r_2s
        r_3 = (np.sqrt(r_p))
        #print(r_3)
        phi_1 = np.arccos(((a_3)**2 - (a_2)**2 - (r_3)**2)/(-2 * a_2 * r_3))
        theta_2a[i] = phi_2 - phi_1
        #theta_2a[i]*=(180/(np.pi))
        phi_3 = np.arccos(((r_3)**2 - (a_2)**2 - (a_3)**2)/(-2 * a_2 * a_3))
        theta_3a[i] = (np.pi * 2) - phi_3
        #theta_3a[i]*=(180/(np.pi))


    theta_3a = np.array(theta_3a)
    theta_1a = np.array(theta_1a)
    theta_2a = np.array(theta_2a)

    print(theta_1a)
    print(theta_2a)
    print(theta_3a)

    #saves the angle values to a csv formatted file
    np.savetxt('theta_1_values.csv', theta_1a, delimiter =',')
    np.savetxt('theta_2_values.csv', theta_2a, delimiter = ',')
    np.savetxt('theta_3_values.csv', theta_3a, delimiter = ',')



    

    #print(theta_1)
    #print(theta_2)
    #print(theta_3)

    #print(theta_1 * 180/(np.pi))
    #print(theta_2 * 180/(np.pi))
    #print(theta_3 * 180/(np.pi))



if __name__ == "__main__":
    main()
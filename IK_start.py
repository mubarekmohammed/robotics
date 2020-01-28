import numpy as np 
import matplotlib.pyplot as plt
import csv
from numpy import asarray


def main():

    y0_3 = 2
    x0_3 = 2
    z0_3 = 0
    a_1 = 10
    a_2 = 10
    a_3 = 10

    x = [2,4,6,4,3,4]
    y = [2,5,7,5,3,2]
    z = [0,2,3,5,1,4]

    theta_1a = [0 for i in range(6)]
    theta_2a = [0 for i in range(6)]
    theta_3a = [0 for i in range(6)]

    for i in range(len(x)):
        theta_1a[i] = np.arctan(y[i]/x[i])
        theta_1a[i]*=(180/(np.pi))
        r_1 = int(np.sqrt((x[i])^2 + (y[i])^2))
        r_2 = z[i] - a_1
        phi_2 = np.arctan(r_2/r_1)
        #print(r_1)
        #print(r_2)
        r_1s = (r_1) ** 2
        r_2s = (r_2) ** 2
        #print(r_1s)
        #print(r_2s)
        r_p = r_1s + r_2s
        r_3 = int(np.sqrt(r_p))
        #print(r_3)
        phi_1 = np.arccos(((a_3)^2 - (a_2)^2 - (r_3)^2)/(-2 * a_2 * r_3))
        theta_2a[i] = phi_2 - phi_1
        theta_2a[i]*=(180/(np.pi))
        phi_3 = np.arccos(((r_3)^2 - (a_2)^2 - (a_3)^2)/(-2 * a_2 * a_3))
        theta_3a[i] = (np.pi * 2) - phi_3
        theta_3a[i]*=(180/(np.pi))

    theta_3a = np.array(theta_3a)
    theta_1a = np.array(theta_1a)
    theta_2a = np.array(theta_2a)

    print(theta_1a)
    print(theta_2a)
    print(theta_3a)
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
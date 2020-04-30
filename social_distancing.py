# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:13:31 2020

@author: Muhammad Junaid Iqbal
@Email: muhammad.junaid@studentpartner.com
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_max = 120  #days
dt = .1   #daystime steps
t = np.linspace(0, t_max, int(t_max/dt) + 1) 
N = 10000  #default population

init_vals = 1 - 1/N, 1/N, 0, 0  

alpha = 0.2
gamma = 0.5 
beta = 1.75 

parameters = alpha, beta, gamma

def social_distance(init_vals, parameters, t, rho):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = parameters
    dt = t[1] - t[0]
    for k in t[1:]:
        next_S = S[-1] - (rho*beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (rho*beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    return S, E, I, R, t



df = pd.DataFrame() 
for rho in (1, 0.8, 0.6):
    print(rho)
    S, E, I, R, t = social_distance(init_vals, parameters, t, rho)
    df['time'+str(rho)] = t
    df['Susceptible '+str(rho)] = S
    df['Exposed '+str(rho)] = E
    df['Infected '+str(rho)] = I
    df['Recovered '+str(rho)] = R
 
print(df.head())


df.plot('time1', y=['Exposed 1', 'Exposed 0.8', 'Exposed 0.6'], 
    color=['darkblue', 'mediumblue', 'blue'])
plt.show()

df.plot('time1', y=['Infected 1','Infected 0.8', 'Infected 0.6'], 
    color=['darkgreen', 'limegreen', 'lime'])
plt.show()



    


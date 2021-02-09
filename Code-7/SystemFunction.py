
# coding: utf-8

# In[ ]:

# Copyright (c) 2020 Hasan Huseyin Sonmez
#
# The following code implements the example given in Oppenheim's Discrete Time Signal Processing 3rd Ed. Section 5.1.2
# it is aimed as a supplementary tool to be used in
# ELM368 Fundamentals of Digital Signal Processing-laboratory course.
# Gebze Technical University, Kocaeli, Turkey
#
# The function parameters are:
#     Input:
#            b : the numerator coefficients of the discrete-time signal/system
#            a : the denominator coefficients of the discrete-time signal/system
#


# In[ ]:

# import the necessary libraries
import numpy as np              # for using basic array functions


# In[ ]:

#w = np.linspace(-np.pi, np.pi, 300)
#Hw, polezz, zerozz, K = SystemFunction(w)


def SystemFunction(w):
    kk = np.arange(1,5,1)
    ck = 0.95*np.exp(1j*(0.15*np.pi+0.02*np.pi*kk));  # coefficients
    z1 = np.exp(-1j*w); # replace z = exp(-jw)
    zs = np.array([.98*np.exp(1j*.8*np.pi), .98*np.exp(-1j*.8*np.pi)]); # zeros of the system
    ps = np.array([.8*np.exp(1j*.4*np.pi), .8*np.exp(-1j*.4*np.pi)]);   # poles of the system
    Hw = (1-zs[0]*z1)*(1-zs[1]*z1) / ((1-ps[0]*z1)*(1-ps[1]*z1));       # initial term
    # calculate the each term in the frequency response as a second order subsystem
    for k in kk:
        dummy = (np.conj(ck[k-1])-z1)*(ck[k-1]-z1) / ((1-ck[k-1]*z1)*(1-np.conj(ck[k-1])*z1))
        Hw = Hw * dummy**2

    polezz = np.concatenate([ck, ck, np.conj(ck), np.conj(ck)])
    zerozz = 1/polezz
    K = 1
    polezz = np.concatenate([polezz, ps])
    zerozz = np.concatenate([zerozz, zs])
    Hw = Hw/3

    return Hw, polezz, zerozz, K


# In[ ]:




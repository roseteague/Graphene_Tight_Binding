#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:03:11 2018

@author: amywang
"""

import numpy as np
import matplotlib.pyplot as plt

def oneDdisorderpotential(x,y,lc,v0):
    """
    Create one-dimensional disorder potentials
    
    Parameters
    ----------
    x : float, array
        The x-position of carbon atoms
    y : float, array
        The y-position of carbon atoms
    lc: float
        The disorder correlation length
    v0: float
        The band velocity of the electrons

        
    Returns
    -------
    Wfinal: float, array
         The final potential at each atom        
    """
    Nx=x.size() #get the number of atoms along x axis
    Ny=y.size() #get the number of atoms along y axis
    hbar=1.054*1E-34
    delta=4*np.pi*hbar*v0/lc
    V=np.random.normal(0,1,Nx) #Create a Gaussian-random distribution array
    C=np.empty((Nx,Nx))
    X1=np.tile(x,(Nx,1))
    X2=X1.T
    C=delta**2*np.exp(-abs(X1-X2)/lc)
    L=np.linalg.cholesky(C)   
    W=np.dot(L,V)
    Wfinal=np.tile(W,(Ny,1))
        
    return Wfinal



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for 2D correlated Gaussian disorder potential on graphene
"""

import numpy as np
import DD_WP_G
from DD_WP_G import *

def twoDdisorderpotential(m,n,lc):
    """
    ============================================================================
    Create one-dimensional disorder potential on graphene lattice
    ============================================================================

    Inputs
    ----------
    m : integer
        Number of atoms along the x-direction

    n : integer
        Number of atoms along the y-direction

    lc : float
        correlation length

    Returns
    -------
    Wfinal: float, array
         The final potential at each atom
    """

    #Calling Crystal to obtain the positions of all carbon atoms.
    points = Crystal(m, n)

    #Exctracting each unique x position.
    X = points[0]
    x_1 = X[0:n*m:n,0]
    x_2 = X[1:n*m:n,0]
    
    #Exctracting each unique y position.
    Y = points[1]
    y = Y[0:n,0]
        
    #Parameters for the strength of the disorder potential in units of eV.
    Delta = 0.3

    #Generating sample of random numbers of Guassian distribution along x axis
    Vx = np.random.normal(0,1,m)
    
    #Generating sample of random numbers of Guassian distribution along y axis 
    Vy = np.random.normal(0,1,n)

    #Generate the two-point matrix for two rows along x axis
    X1 = np.tile(x_1,(m,1))
    X2 = X1.T
    X3 = np.tile(x_2,(m,1))
    X4 = X3.T
    
    #Generate the two-point matrix for y axis
    X5 = np.tile(y,(n,1))
    X6 = X5.T

    #Generate the two-point spatial correlation matrix for x (two rows) and y axis
    Cx1 = Delta**2*np.exp(-abs(X1-X2)/lc)
    Cx2 = Delta**2*np.exp(-abs(X3-X4)/lc)
    Cy = Delta**2*np.exp(-abs(X5-X6)/lc)

    #Cholesky decomposition of the two-point correlation matrix and generate the final random vector
    Lx1 = np.linalg.cholesky(Cx1)
    Wx1 = np.dot(Lx1,Vx)
    Lx2 = np.linalg.cholesky(Cx2)
    Wx2 = np.dot(Lx2,Vx)
    Ly = np.linalg.cholesky(Cy)
    Wy = np.dot(Ly,Vy)

    #Put the potentials on all atoms and reshape them to the requried output format
    Wxf=np.zeros((n,m))
    Wyf=np.zeros((n,m))
    
    Wxf[0:n:2,0:m]= Wx1
    Wxf[1:n:2,0:m]= Wx2
    Wxfinal=Wxf.T.reshape((n*m,1))
    
    
    Wyf[:,0:m]=Wy.reshape((n,1))
    Wyfinal=Wyf.T.reshape((n*m,1))
    
    #The final potential for each atom is the sum of the x- and y- potential component
    Wfinal=Wxfinal+Wyfinal
    
    return Wfinal

if __name__ == "__main__":
    twoDdisorderpotential(10,10,10)

"""
Main program for studying the propagation of a Gaussian wavepacket through 2D
crystals using the Tight Binding Method.
"""

import math
import matplotlib.pyplot as plt

# Describe system for use in image/video titles
def TB(lattice,V,animate=False):
    """
    ===========================================================================
    Main file for the split operator tight binding solver
    ===========================================================================

    This function collects all modules which define the lattice, the initial
    wavepacket, the Tight Binding Hamiltonian and the full split operator
    solver. It applies the same parameters to each module and allows the program
    to be run from one place.

    The following variables are defined on lines ___ to ___:
    the size of the system, the correlation length, the
    width of the Gaussian packet, the momentum eigenvalues in x and y and the
    time intervals and length to be simulated can be adjusted. These can be
    changed to simulate different conditions.

    Inputs
    -----------
    lattice - string
            - description of the lattice to be modelled. This can be either
                'square' or 'graphene'.

    V       - string
            - description of the potential to be used on the system. This can be
                either 'None', 'one dimensional' or 'two dimensional'.

    animate - boolean
            - Determines whether or not a .mp4 file of the propagation will be
                produced. N.B this takes more time so should only be set if it
                is necessary to study the propagation.

    Returns
    ----------
    N.A

    If 'animate' is set to be true, an .mp4 file will be saved.
    A plot of the final state of the wavepacket will be displayed as a contour
        plot where the colour represents the amplitude.
    """

    # System parameters: can be modified
    m = 500                     # Number of atoms along x
    n = 500                     # Number of atoms along y
    lc = 1                      # Correlation length for disorder potential
    s = 5*lc                    # Width of initial Gaussian wavepacket
    kx = math.pi/(5*lc)         # Momentum eigenvalue (wavenumber) along x
    ky = math.pi/(5*lc)         # Momentum eigenvalue (wavenumber) along x
    dt = 0.1e-15                # Time interval to be sampled
    T = 5e-15                   # Total time of wavepacket propagation
    Ns = round(T/dt) + 1        # Integer number of time steps


    # Import the full (fast) Hamiltonian solver
    from DD_TB_S import TB_solver_S                         # Solver module

    if lattice == 'square':
        # Import system modules for Square lattice
        from DD_WP_S import Crystal                         # Wavefunction module
        from DD_WP_S import Psi                             # Wavefunction module
        from DD_DP_S import oneDdisorderpotential           # Potential module
        from DD_DP_S2 import twoDdisorderpotential          # Potential module
        from DD_SH import TBH                               # Hamiltonian module


    if lattice == 'graphene':
        # Import system modules for Graphene (hexagonal) lattice
        from DD_WP_G import Crystal                         # Wavefunction module
        from DD_WP_G import Psi                             # Wavefunction module
        from DD_DP_G import oneDdisorderpotential           # Potential module
        from DD_DP_G2 import twoDdisorderpotential          # Potential module
        from DD_GH import TBH                               # Hamiltonian module



        #Need to have some assert statements here ...

    # Run the system modules to descibe the lattice and initial wavepacket
    pos = Crystal(n,m)
    wfc = Psi(s,kx,ky,n,m,pos)

    # Run the potential module for the system to be simulated
    if V == 'None':
        # If the system is to be run with no external potential, assign an
        # arbitrary value of 1 to the potential variable.
        DP = 1

    if V == 'one dimensional':
        DP = oneDdisorderpotential(m,n,lc,pos)

    if V == 'two dimensional':
        DP = twoDdisorderpotential(m,n,lc,pos)

    # Run the Hamiltonian module for the system
    H = TBH(DP,n,m,dt,V)

    if animate:
    # Solves the tight binding hamiltonian using a split operator method
    # described in the file DD_TB_S. Records an image after each time step and
    # compiles into an mp4 movie file.
        from animate import MakeMovie

        pd = TB_solver_S(n,m,pos,wfc,H,T,dt,animate)
        MakeMovie('Tight Binding in ' + lattice + ' with ' + V + ' potential')
    else:
    # Solves the tight binding hamiltonian using a split operator method
    # describes in the file DD_TB_S
        pd = TB_solver_S(n,m,pos,wfc,H,T,dt,animate)

    #Plotting
    # plt.contourf(pos[0].reshape((n,m)),pos[1].reshape((n,m)), pd, 100, cmap = 'gnuplot')
    # plt.title('n='+str(n)+' m='+str(m)+' t='+str(Ns*0.1)+'fs')
    # plt.show()

def TBS(lattice,V, animate = False):
    """
    ===========================================================================
    Main file for the simple split operator tight binding solver
    ===========================================================================

    This function collects all modules which define the lattice, the initial
    wavepacket, the Tight Binding Hamiltonian and the full split operator
    solver. It applies the same parameters to each module and allows the program
    to be run from one place.

    The following variables are defined on lines ___ to ___:
    the size of the system, the correlation length, the
    width of the Gaussian packet, the momentum eigenvalues in x and y and the
    time intervals and length to be simulated can be adjusted. These can be
    changed to simulate different conditions.

    Inputs
    -----------
    lattice - string
            - description of the lattice to be modelled. This can be either
                'square', 'graphene', or '1D square'.

    V       - string
            - description of the potential to be used on the system. This can be
                either 'None', 'one dimensional' or 'two dimensional'.
                If the lattice is '1D square', the potential MUST be 'None'

    animate - boolean
            - Determines whether or not a .mp4 file of the propagation will be
                produced. N.B this takes more time so should only be set if it
                is necessary to study the propagation.

    Returns
    ----------
    N.A

    If 'animate' is set to be true, an .mp4 file will be saved.
    A plot of the final state of the wavepacket will be displayed as a contour
        plot where the colour represents the amplitude.
    """

    # System Parameters
    m = 100                     # Number of atoms along x
    n = 100                     # Number of atoms along y
    lc = 2                      # Correlation length for disorder potential
    s = 5*lc                    # Width of initial Gaussian wavepacket
    kx = math.pi/(5*lc)         # Momentum eigenvalue (wavenumber) along x
    ky = math.pi/(5*lc)         # Momentum eigenvalue (wavenumber) along x
    dt = 0.1e-15                # Time interval to be sampled
    T = 4e-15                   # Total time of wavepacket propagation
    Ns = round(T/dt) + 1        # Integer number of time steps


    # Import the simple Hamiltonian solver
    from DD_SS import TB_ss                                 # Solver module


    if lattice == 'square':
        # Import modules for Square lattice
        from DD_WP_S import Crystal                         # Wavefunction module
        from DD_WP_S import Psi                             # Wavefunction module
        from DD_DP_S import oneDdisorderpotential           # Potential module
        from DD_DP_S2 import twoDdisorderpotential          # Potential module
        from DD_FH_S import FTBH                            # Hamiltonian module

    if lattice == 'graphene':
        # Import modules for Graphene lattice
        from DD_WP_G import Crystal                         # Wavefunction module
        from DD_WP_G import Psi                             # Wavefunction module
        from DD_DP_G import oneDdisorderpotential           # Potential module
        from DD_DP_G2 import twoDdisorderpotential          # Potential module
        from DD_FH_G import FTBH                            # Hamiltonian module

    if lattice == '1D square':
        # Import modules for 1D square lattice
        # Must have no potential for this 1D solver
        from DD_1D_modified import Crystal                  # Crystal Module
        from DD_1D_modified import Psi                      # Wavefunction Module
        from DD_1D_modified import TBH                      # Hamiltonian Module
        from DD_1D_modified import TB_ss                    # Solver Module


    # Run the system modules to descibe the lattice and initial wavepacket
    pos = Crystal(n,m)
    wfc = Psi(s,kx,ky,n,m,pos)

    # Run the potential module for the system to be simulated
    if V == 'None':
        # If the system is to be run with no external potential, assign an
        # arbitrary value of 1 to the potential variable.
        DP = 1

    if V == 'one dimensional':
        DP = oneDdisorderpotential(m,n,lc,pos)

    if V == 'two dimensional':
        DP = twoDdisorderpotential(m,n,lc,pos)

    # Run the Hamiltonian module for the system
    FH = FTBH(DP,n,m,dt,V)

    if animate:
    # Solves the tight binding hamiltonian using a split operator method
    # described in the file DD_TB_S. Records an image after each time step and
    # compiles into an mp4 movie file.
        from animate import MakeMovie

        pd = TB_ss(n,m,pos,wfc,FH,T,dt,animate)
        MakeMovie('Tight Binding in ' + lattice + ' with ' + V + ' potential')
    else:
    # Solves the tight binding hamiltonian using a split operator method
    # described in the file DD_TB_S.
    # why does the solver take the DP argument?
        pd = TB_ss(n,m,pos,wfc,FH,T,dt)

    plt.contourf(pos[0].reshape((n,m)),pos[1].reshape((n,m)), pd, 100, cmap = 'gnuplot')
    plt.title('n='+str(n)+' m='+str(m)+' t='+str(Ns*0.1)+'fs')
    plt.show()


if __name__ == '__main__':
    TB('graphene', 'one dimensional')

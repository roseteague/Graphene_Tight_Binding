"""Module for 2 D problem
"""

import numpy as np
from scipy.sparse.linalg import expm_multiply

def TB_ss(n, m, pos, wfc, H, DT, dt):
    """Split operator technique for propogation of wave packets with square
        lattice tight-binding hamiltonian.

    """

    Ns = round(DT/dt) + 1

    for i in range(Ns):

        wfc = expm_multiply(H, wfc)

    wvf_c = np.conjugate(wfc)

    pd = np.multiply(wvf_c, wfc)
    pd = np.reshape(pd,(n,m))

    return pd

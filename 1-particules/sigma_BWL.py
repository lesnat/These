# coding:utf8
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Plot formats
plt.close("all")
plt.ion()
plt.style.use("bmh")
rcParams['figure.figsize'] = [9.5, 5.10]
# rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

#
me = 0.511
def sigma_BWL(s):
    r"""
    Section efficace Breit-Wheeler linéaire (en re^2).

    Parameters
    ----------
    s : {float, array of float}
        Variable de Mandelstam de masse invariante, en MeV^2.

    References
    ----------
    W. Greiner and J. Reinhardt, Quantum Electrodynamics, 4th ed (Springer, Berlin, 2009).
    """
    sigma   = 4*np.pi/s * me**2 * ((2 + 8*me**2/s - 16*me**4/s**2) * np.log((np.sqrt(s) + np.sqrt(s - 4*me**2))/(2*me)) - np.sqrt(1 - 4*me**2/s) * (1 + 4*me**2/s))

    return np.nan_to_num(sigma)

#
s = np.logspace(-2,4,1000)

plt.figure(0)
plt.plot(np.sqrt(s), sigma_BWL(s), color="k")
plt.ylabel(r"$\sigma_{\gamma\gamma}$ [$r_e^2$]")
plt.xlabel(r"$\sqrt{s}$ [$MeV$]")
plt.xscale("log")
plt.xlim(1e-1, 1e2)
plt.ylim(0, 2.5)
plt.savefig("sigma_BWL_s.png")

plt.figure(1)
E = np.linspace(0, 15, 5000)
for psi12 in [20, 45, 90, 180]:
    s = 2*E**2 * (1-np.cos(np.radians(psi12)))
    plt.plot(E, sigma_BWL(s), label="$\psi_{12}=%d$ deg"%psi12)

plt.legend()
plt.ylabel(r"$\sigma_{\gamma\gamma}$ [$r_e^2$]")
plt.xlabel(r"$E_1=E_2$ [$MeV$]")
plt.xlim(0, 15)
plt.ylim(0,2.5)
plt.savefig("sigma_BWL_energies.png")

# coding:utf8
"""

"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Plot formats
plt.close("all")
plt.ion()
plt.style.use("bmh")
rcParams['figure.figsize'] = [9.5, 5.10]
# rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

from matplotlib.colors import LogNorm
from scipy.special import gamma

# Electron mass energy
me = 0.511

def g_Brem(EoverK):
    r"""
    Function g for Exponential energy distribution.

    Parameters
    ----------
    EoverK : {float, array}
        Gamma energy over characteristic energy.
    """
    return np.exp(-EoverK)

def g_LMC(EoverK):
    r"""
    Function g for Synchrotron-like energy distribution.

    Parameters
    ----------
    EoverK : {float, array}
        Gamma energy over characteristic energy.
    """
    return (EoverK)**(-0.95) * np.exp(-EoverK)/gamma(-0.95+1)

def sigma_LBW(s):
    # Compute the Breit-Wheeler cross section in term of s
    sigma   = 4*np.pi/s * me**2 * ((2 + 8*me**2/s - 16*me**4/s**2) * np.log((np.sqrt(s) + np.sqrt(s - 4*me**2))/(2*me)) - np.sqrt(1 - 4*me**2/s) * (1 + 4*me**2/s))

    # Return the result
    return np.nan_to_num(sigma)

# Define F
def F(E1, K1, g1, E2, K2, g2, psi12):
    return g1(E1/K1)/K1 * g2(E2/K2)/K2 * sigma_LBW(2*E1*E2*(1-np.cos(np.radians(psi12))))

# Define grid of E1 and E2
E1  = np.logspace(-2,2,2000)
E2  = np.logspace(-2,2,2001)
gE1, gE2 = np.meshgrid(E1, E2, indexing='ij')

# Define configurations
parameters  = [
    dict(label="I"  , config="Brem-Brem", psi12 = 90    , K1=2.00       , K2 = 2.00     , g=g_Brem),
    dict(label="II" , config="LMC-LMC"  , psi12 = 90    , K1=3.00       , K2 = 3.00     , g=g_LMC),
    dict(label="III", config="LMC-LMC"  , psi12 = 90    , K1=3.00       , K2 = 15.0     , g=g_LMC)
]

plt.figure(figsize=(17, 5))
for i, p in enumerate(parameters):

    # Retrieve the values of the maximum
    res = F(gE1, p["K1"], p["g"], gE2, p["K2"], p["g"], p["psi12"])
    idmax = np.where(res == np.max(res))
    e1p = float(E1[idmax[-2]])
    e2p = float(E2[idmax[-1]])

    plt.subplot(1, 3, i+1)
    map=plt.pcolormesh(gE1, gE2, res, norm=LogNorm(vmin=1e-6, vmax=5e-1))
    plt.plot(e1p, e2p, marker='o', color="k")

    mu = 1 - np.cos(np.radians(p["psi12"]))
    plt.plot(E1, (2*0.511)**2/(2*E1*mu), color='k', linestyle="-", linewidth=3)
    plt.text(0.21, 0.21, r"$\sigma_{\gamma\gamma}=0$", rotation=-45, color='k')
    plt.plot(E1, 2.06/(2*E1*mu), color='#A60628', linestyle="--", linewidth=3)
    plt.text(0.32, 0.32, r"$\sigma_{\gamma\gamma}=\max(\sigma_{\gamma\gamma})$", rotation=-45, color='#A60628')
    plt.plot(E1, 71.8/(2*E1*mu), color='w', linestyle="-.", linewidth=3)
    plt.text(1.5, 1.5, r"$\sigma_{\gamma\gamma}=\max(\sigma_{\gamma\gamma})/10$", rotation=-45, color='w')

    print("################################################################################")
    print(p["label"])
    print(e1p, e2p)
    print("\n")

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel(r"$E_1$ [$MeV$]")

    plt.xlim(min(E1), max(E1))
    plt.ylim(min(E2), max(E2))

    plt.subplot(1, 3, 1)
    plt.ylabel(r"$E_2$ [$MeV$]")
    plt.title("(a)")
    plt.subplot(1, 3, 2)
    plt.title("(b)")
    plt.subplot(1, 3, 3)
    plt.title("(c)")

plt.savefig("cinematique_validation_nocolorbar.png")

plt.figure(figsize=(17, 5))
plt.colorbar(map)
plt.savefig("cinematique_validation_colorbar.png")

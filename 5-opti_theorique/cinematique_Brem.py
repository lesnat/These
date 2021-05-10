# coding:utf8
r"""
Compare the results of the model for leading energy couple with numerical results, for two Brem sources.
"""
# Import modules
# coding:utf8

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.special import gamma

# Format the plots
plt.close("all")
plt.ion()
plt.style.use("bmh")
rcParams['figure.figsize'] = [9.5, 5.10]
# rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

# Electron mass energy
me = 0.511

from matplotlib.colors import LogNorm
from matplotlib.lines import Line2D


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

def h(zeta, A, B, n, m):
    r"""
    Fit function (values in re^2) for the LBW equivalent cross section.

    Parameters
    ----------
    zeta : float
        Characteristic center of mass energy squared, in MeV^2.
    A,B : float
        Fit parameters, in MeV^2.
    n,m : float
        Fit indexes.
    """
    return A/zeta**n * np.exp(-B/zeta**m)

def beaming_condition_satisfied(Et, Ecm):
    r"""
    Compute the beaming condition.
    Parameters
    ----------
    Et : array
        Total energy of the collision in the lab frame
    Ecm : array
        CM energy
    """
    if 2*me * Et/Ecm**2 > 1:
        return True
    else:
        return False

def compute_angular_bound(Et, Ecm):
    r"""
    Returns the maximum half angle associated with given total energy and CM energy.

    Parameters
    ----------
    Et : array
        Total energy of the collision in the lab frame
    Ecm : array
        CM energy
    """
    psipmax = np.arctan2(Ecm * np.sqrt(Ecm**2 - 4*me**2), np.sqrt((2*me*Et)**2 - Ecm**4))
    return psipmax

def compute_solid_angle(Et, Ecm):
    r"""
    Returns the typical solid angle of the positron source in the lab frame.

    Parameters
    ----------
    Et : array
        Total energy of the collision in the lab frame
    Ecm : array
        CM energy
    """
    psipmax = compute_angular_bound(Et, Ecm)
    omegap = 2*np.pi*(1-np.cos(psipmax))
    return omegap


def compute_energy_typical(Et):
    r"""
    Returns the typical energy associated with given total energy and CM energy.

    Parameters
    ----------
    Et : array
        Total energy of the collision in the lab frame
    """
    Eptyp = Et/2
    return Eptyp

# Define G
def G(E1, K1, E2, K2, psi12):
    return g_Brem(E1/K1) * g_Brem(E2/K2) * sigma_LBW(2*E1*E2*(1-np.cos(psi12)))

# Define the grid of energies
E1  = np.logspace(-2,2,2000)
E2  = np.logspace(-2,2,2001)
# E1  = np.logspace(-2,2,1000)
# E2  = np.logspace(-2,2,1001)
gE1, gE2 = np.meshgrid(E1, E2, indexing='ij')

# Define colors
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']

# Define asymmetry coefficients and collision angles
energies = np.linspace(1,6,6)
# energies = [0.5, 1.0, 5.0]
angles = np.radians(range(1,180,1))
# angles = np.radians(range(5,180,5))

# Loop over all the configurations
for Ki, color in zip(energies, colors):
    # Initialize numerical optimum energies and theoretical optimum energies
    Np = []
    psipmax = []
    Eptyp = []
    for psi12 in angles:
        # Print informations on the current configuration
        print(r"################################################################################")
        print("psi12 = {:.4g} deg".format(np.degrees(psi12)))
        print("Ki = {:.4g}".format(Ki))

        # Compute characteristic energies
        K1  = Ki # MeV
        K2  = Ki # MeV

        zeta = 2 * K1 * K2 * (1-np.cos(psi12))
        sigma = h(zeta, 23.3, 3.94, 0.674, 0.374)
        L12 = (1-np.cos(psi12))/np.sin(psi12)
        Np.append(L12*sigma)

        # Get leading energy couple from numerical results
        res = G(gE1, K1, gE2, K2, psi12)
        idmax = np.where(res == np.max(res))
        e1p = float(E1[idmax[-2]])
        e2p = float(E2[idmax[-1]])

        Etp = e1p + e2p
        Ecmp = np.sqrt(2 * e1p * e2p * (1-np.cos(psi12)))
        if beaming_condition_satisfied(Etp, Ecmp):
            psipmax.append(compute_angular_bound(Etp, Ecmp))
            Eptyp.append(compute_energy_typical(Etp))
        else:
            psipmax.append(np.nan)
            Eptyp.append(np.nan)


    # Plot results
    plt.figure(0)
    plt.plot(np.degrees(angles), Np, '-', c=color, label="$K={:.1f} ~ MeV$".format(Ki))
    plt.figure(1)
    plt.plot(np.degrees(angles), np.degrees(psipmax), '-', c=color)
    plt.figure(2)
    plt.plot(np.degrees(angles), Eptyp, '-', c=color)

# Format the plots
plt.figure(0)
plt.xlabel(r"$\psi_{12}$ [$deg$]")
plt.ylabel(r"$N_+ \times (aL/r_e^2 N_1 N_2)$")
plt.yscale("log")
plt.legend(ncol=2)
plt.ylim(1e-2, 1e2)
plt.xlim(0, 180)
plt.savefig("cinematique_optimisation_Np.png")

plt.figure(1)
plt.xlabel(r"$\psi_{12}$ [$deg$]")
plt.ylabel(r"$\psi_+^{max}$ [$deg$]")
plt.ylim(0, 90)
plt.xlim(0, 180)
plt.savefig("cinematique_optimisation_psipmax.png")

plt.figure(2)
plt.xlabel(r"$\psi_{12}$ [$deg$]")
plt.ylabel(r"$E_+^{typ}$ [$MeV$]")
plt.yscale("log")
plt.ylim(4e-1, 4e1)
plt.xlim(0, 180)
plt.axhline(0.511, ls='--', color='k')
plt.text(160, 0.55, r"$m_e c^2$")
plt.savefig("cinematique_optimisation_Eptyp.png")

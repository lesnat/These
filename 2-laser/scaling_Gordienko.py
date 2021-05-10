# coding:utf8
"""
All units are in SI, except the power in TW and the energies in MeV

References
----------
S. Gordienko and A. Pukhov, Scalings for Ultrarelativistic Laser Plasmas and Quasimonoenergetic Electrons, Physics of Plasmas 12, 043109 (2005).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Plot formats
plt.close("all")
plt.ion()
plt.style.use("bmh")
# rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

# Define constants
c       = 3e8                       # light speed in vacuum
re      = 2.8e-15                   # electron classical radius
me      = 0.511                     # electron mass energy in MeV
Prel    = 8.5e-3                    # natural relativistic power in TW
# Define laser parameters
tau_L   = 30e-15                    # laser pulse duration
lambda_L= 1.0e-6                    # laser wavelength
P_L     = np.logspace(0, 3, 1000)   # laser power in TW

# Compute energy and number of LWFA accelerated electrons in the bubble regime
Emono = 0.65 * me * np.sqrt(P_L/Prel) * c * tau_L / lambda_L
Nmono = (1.8 * lambda_L/(re * 2 * np.pi)) * np.sqrt(P_L/Prel)

# Plot results
plt.figure()
plt.subplot(211)
plt.plot(P_L, Emono, color="#1f77b4")
plt.ylabel(r"$E_{e}^{bulle}$ [$MeV$]")
plt.yscale("log")
plt.xscale("log")
plt.ylim(30, 3e3)
plt.xlim(1, 1000)
plt.subplot(212)
plt.plot(P_L, Nmono, color="#ff7f0e")
plt.yscale("log")
plt.ylabel("$N_{e}^{bulle}$")
plt.xscale("log")
plt.ylim(5e8, 5e10)
plt.xlim(1, 1000)
plt.xlabel("$P_0$ [$TW$]")
a=plt.twinx()
a.set_yscale("log")
a.set_ylim(1e9*5e8*1.6e-19, 1e9*5e10*1.6e-19)
a.set_ylabel("$Q_{e}^{bulle}$ [$nC$]")


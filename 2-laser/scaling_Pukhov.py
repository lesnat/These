# coding:utf8
"""
All units are in SI, except the power in TW and the energies in MeV

References
----------
A. Pukhov, Z.-M. Sheng, and J. Meyer-ter-Vehn, Particle Acceleration in Relativistic Laser Channels, Physics of Plasmas 6, 2847 (1999).
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

# Define laser parameters
tau_L   = 30e-15                    # laser pulse duration
d_L     = 10e-6                     # laser waist
lambda_L= 1.0e-6                    # laser wavelength
P_L     = np.logspace(0, 3, 1000)   # laser power in TW
E_L     = P_L * 1e-3 * tau_L * 1e15/0.94
I0      = 8.8e22 * P_L*1e-3/(d_L*1e6)
a0      = 0.85 * lambda_L * 1e6 * np.sqrt(I0/1e18)

# Compute typical energy and number of electrons produced by DLA
Te = 1.5e-9*np.sqrt(I0)
Ne = 0.3*E_L/(Te*1e6*1.6e-19)

# Plot results
plt.figure()
plt.subplot(211)
plt.plot(P_L, Te, color="#1f77b4")
plt.ylabel(r"$T_{e}^{AD}$ [$MeV$]")
plt.yscale("log")
plt.xscale("log")
plt.ylim(0, 200)
plt.xlim(1, 1000)
plt.subplot(212)
plt.plot(P_L, Ne, color="#ff7f0e")
plt.yscale("log")
plt.ylabel(r"$N_{e}^{AD}$")
plt.xscale("log")
plt.ylim(1e10, 1e12)
plt.xlim(1, 1000)
plt.xlabel("$P_0$ [$TW$]")
a=plt.twinx()
a.set_yscale("log")
a.set_ylim(1e9*1e10*1.6e-19, 1e9*1e12*1.6e-19)
a.set_ylabel(r"$Q_{e}^{AD}$ [$nC$]")


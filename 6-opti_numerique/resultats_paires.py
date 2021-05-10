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
#rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['figure.figsize'] = [10, 10]
# rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

I0 = [1e19, 1e20, 1e21]
nf1 = [2.57e-5, 2.20e-3, 8.18e-2]
nf5 = [1.97e-5, 4.29e-3, 3.62e-1]
rr1 = 5.62690e-3
rr5 = 2.60395e-2

plt.figure()
I = np.logspace(18, 22, 1000)

Ng_th=3e10*(I/1e20)
Np_th=(Ng_th)**2/(400e-4+2*250e-4*np.tan(np.radians(40)))**2 * (2.8e-13)**2
plt.plot(I, Np_th, color='#467821', linestyle='-', linewidth=3)
plt.text(8e18, 1e-4, r"Modèle chap. 5", fontsize="18", color='#467821', rotation=45)

E = (I/8.8e22) * 25 * 30/0.94
plt.plot(I, 1e8*(0.0025*E)**2/(250**2 * (1-np.cos(np.radians(40)))), ls='-.', lw=3, color='#0072B2')
plt.text(6.2e18, 2.1e-4, r"Ribeyre et al., 2016", fontsize="18", color='#0072B2', rotation=45)

plt.plot(I0, nf1, marker="<", color="#D8334A", linestyle=":", lw=3.5, ms=10, label="Simulations, $N_{fils}=1$")
plt.plot(I0, nf5, marker="o", color="#8067B7", linestyle=":", lw=3.5, ms=10, label="Simulations, $N_{fils}=5$")

plt.xscale("log")
plt.yscale("log")

plt.xlabel(r"$I_0$ [$W/cm^2$]")
plt.ylabel(r"$N_+/tir$")

plt.xlim(5e18, 5e21)
plt.ylim(1e-5, 10)

plt.legend(loc=4, ncol=1)

ay=plt.twiny()
ay.set_xscale("log")
ay.set_xlim((5e18/8.8e22) * 25 * 30/0.94, (5e21/8.8e22) * 25 * 30/0.94)
ay.set_xlabel(r"$E_L$ [$J$]")
plt.grid(False)

plt.savefig("resultats_paires.png")


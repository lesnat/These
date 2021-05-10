# coding:utf8
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# Format plots
plt.close("all")
plt.ion()
plt.style.use("bmh")
rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

#
psi12=np.linspace(1e-3, 180-1e-3, 1000)
plt.plot(psi12, (1-np.cos(np.radians(psi12)))/np.sin(np.radians(psi12)), "k")
plt.ylabel(r"$\mathcal{L}_{12}^{sc} \times (a L/N_1 N_2)$")
plt.xlabel(r"$\psi_{12}$ [$deg$]")
plt.yscale("log")
plt.xlim(0,180)
plt.ylim(1e-2, 1e2)
plt.savefig("angle_luminosite.png")

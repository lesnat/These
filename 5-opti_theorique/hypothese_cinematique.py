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

E=np.linspace(0,5,100)
K1 = K2 = 2.
E1p = E2p = 0.92

plt.figure(0)
plt.plot(E, np.exp(-E/K1)/K1, color='#348ABD', lw=3)
plt.axvline(E1p, color="k", ls="--", lw=3)
plt.yscale("log")
plt.xlabel(r"$E_1$ [$MeV$]")
plt.ylabel("$f_1(E_1)$ [$MeV^{-1}$]")
plt.title("Faisceau 1")
plt.legend(("Brem", "Modèle"))
plt.xlim(min(E),max(E))
plt.ylim(1e-2, 1)
plt.savefig("hypothese_cinematique_1.png")


plt.figure(1)
plt.plot(E, np.exp(-E/K2)/K2, color='#A60628', lw=3)
plt.axvline(E2p, color="k", ls="--", lw=3)
plt.yscale("log")
plt.xlabel(r"$E_2$ [$MeV$]")
plt.ylabel("$f_2(E_2)$ [$MeV^{-1}$]")
plt.title("Faisceau 2")
plt.legend(("Brem", "Modèle"))
plt.xlim(min(E),max(E))
plt.ylim(1e-2, 1)
plt.savefig("hypothese_cinematique_2.png")

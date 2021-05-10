# coding:utf8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Format plots
plt.close("all")
plt.ion()
plt.style.use("bmh")
# rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

from matplotlib.colors import LogNorm
from matplotlib.lines import Line2D

import xcom

energy = np.array([ 1.0E+04, 1.5E+04, 2.0E+04, 3.0E+04, 4.0E+04,
                    5.0E+04, 6.0E+04, 8.0E+04, 1.0E+05, 1.5E+05, 2.0E+05, 3.0E+05,
                    4.0E+05, 5.0E+05, 6.0E+05, 8.0E+05, 1.0E+06, 1.022E+06, 1.25E+06,
                    1.5E+06, 2.0E+06, 2.044E+06, 3.0E+06, 4.0E+06, 5.0E+06, 6.0E+06,
                    7.0E+06, 8.0E+06, 9.0E+06, 1.0E+07, 1.1E+07, 1.2E+07, 1.3E+07,
                    1.4E+07, 1.5E+07, 1.6E+07, 1.8E+07, 2.0E+07, 2.2E+07, 2.4E+07,
                    2.6E+07, 2.8E+07, 3.0E+07, 4.0E+07, 5.0E+07, 6.0E+07, 8.0E+07,
                    1.0E+08, 1.5E+08, 2.0E+08, 3.0E+08, 4.0E+08, 5.0E+08, 6.0E+08,
                    8.0E+08, 1.0E+09], dtype='d') # Énergie en eV


Z = [6, 13, 29, 47, 78]
for i, z in enumerate(Z):
    data = xcom.calculate_attenuation(xcom.Material([z]))

    # Affiche les coefficients d'atténuations des matériaux choisis
    plt.figure(i)
    plt.plot(data["energy"]/1e6, data["photoelectric"], label="Photo-électrique", color="#A60628", linestyle="--", linewidth=2)
    plt.plot(data["energy"]/1e6, data["coherent"], label="Rayleigh", color="#7A68A6", linestyle='-.', linewidth=2)
    plt.plot(data["energy"]/1e6, data["incoherent"], label="Compton", color="#467821", linestyle=':', linewidth=2)
    plt.plot(data["energy"]/1e6, data["pair_atom"], label="Bethe-Heitler", color="#348ABD", linestyle="--", linewidth=2)
    plt.plot(data["energy"]/1e6, data["pair_electron"], label="Triplet", color="#D55E00", linestyle="-.", linewidth=2)
    plt.plot(data["energy"]/1e6, data["total"], color="k", linewidth=3)

    plt.gca().add_artist(plt.legend(loc=1))
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$E_\gamma$ [$MeV$]")
    plt.ylabel(r"Coefficient d'atténuation [$cm^2/g$]")
    plt.xlim(1e-2, 1e3)
    plt.ylim(1e-4, 1e3)
    plt.gca().add_artist(plt.legend((Line2D([0],[0],marker="None",ls="-",c='k', lw=3),), ("Total",), loc=3))
    plt.title("Z = {}".format(z))
    
    plt.savefig("photons_Z{:d}.png".format(z))

# Affiche les coefficient d'atténuation totaux en fonction du numéro atomique
Z = range(1,101)
gZ, gE = np.meshgrid(Z, energy/1e6, indexing='ij')

# Initialise les listes de valeurs de coeff. d'attenuation, et les listes de transition entre les processus 
photoelectric, coherent, incoherent, pair_electron, pair_atom, total = [], [], [], [], [], []

photoelectric_incoherent_transition = []
incoherent_pair_transition = []

# Récupère les coeff. d'attenuation pour tout les processus + les transitions, pour chaque matériau
for z in Z:
    data = xcom.calculate_attenuation(xcom.Material([z]), energy)

    photoelectric.append(data["photoelectric"])
    coherent.append(data["coherent"])
    incoherent.append(data["incoherent"])
    pair_electron.append(data["pair_electron"])
    pair_atom.append(data["pair_atom"])
    total.append(data["total"])

    photoelectric_incoherent_transition.append(min(energy[data["photoelectric"]<data["incoherent"]]/1e6))
    incoherent_pair_transition.append(min(energy[data["incoherent"]<(data["pair_atom"]+data["pair_electron"])]/1e6))

# Affiche les résultats
plt.figure(6, figsize=(8.27, 11.67))
plt.subplots_adjust(bottom=0., top=0.9, wspace=0., hspace=0.)
levels = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.13, 0.2, 0.3, 0.5, 1, 3, 10, 50, 100, 500, 1000, 5000, 10000]
plt.pcolormesh(gZ, gE, total, norm=LogNorm())
plt.colorbar(orientation="horizontal", label=r"Coefficient d'atténuation total [$cm^2/g$]")
plt.clabel(plt.contour(gZ, gE, total, norm=LogNorm(), levels=levels, colors="k", linewidths=1), levels ,fmt="%.3g", fontsize=8)
plt.yscale("log")
plt.xlabel(r"$Z$")
plt.ylabel(r"$E_\gamma$ [$MeV$]")

plt.plot(Z, photoelectric_incoherent_transition, color="#A60628", linewidth=3)
plt.plot(Z, incoherent_pair_transition, color="#348ABD", linewidth=3)

plt.axvline(6, color="k", linestyle="--")
plt.text(6, 1.1e3, "C")
plt.axvline(13, color="k", linestyle="--")
plt.text(13, 1.1e3, "Al")
plt.axvline(29, color="k", linestyle="--")
plt.text(29, 1.1e3, "Cu")
plt.axvline(47, color="k", linestyle="--")
plt.text(47, 1.1e3, "Ag")
plt.axvline(78, color="k", linestyle="--")
plt.text(78, 1.1e3, "Pt")

plt.text(101, 8, "Prod. paires domine", rotation=90, color="#348ABD")
plt.text(105, 0.45, "Compton domine", rotation=90, color="#467821")
plt.text(101, 1.1e-2, "Photo-électrique domine", rotation=90, color="#A60628")

plt.savefig("photons_E_Z.png")

# coding:utf8

import numpy as np
import mendeleev as md

import matplotlib.pyplot as plt
from matplotlib import rcParams

# Plot formats
plt.close("all")
plt.ion()
plt.style.use("bmh")
# rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['figure.figsize'] = [7.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

from matplotlib.lines import Line2D

# https://www.physics.nist.gov/cgi-bin/Star/compos.pl

# Idea : color for metal, metaloid, ... and marker shape for solid, liquid, gaz in STP

symbols = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P",
            "S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
            "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh",
            "Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
            "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re",
            "Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
            "Pa","U","Np","Pu","Am","Cm","Bk","Cf"]

state = []
rho = []
series = []
for symb in symbols:
    elem = md.element(symb)
    try:
        if elem.boiling_point < 300:
            state = "gas"
            rho = elem.density * 1.205e-3
            marker = "s"
        elif elem.melting_point < 300:
            state = "liquid"
            rho = elem.density * 1.00
            marker = "o"
        else:
            state = "solid"
            rho = elem.density * 1.00
            marker = "v"

        ni = rho/(elem.mass/6.022e23)
        ne = elem.atomic_number * ni

        if elem.series == "Nonmetals":
            color='#348ABD'
        elif elem.series == "Noble gases":
            color='#A60628'
        elif elem.series == "Alkali metals":
            color='#7A68A6'
        elif elem.series == "Alkaline earth metals":
            color='#467821'
        elif elem.series == "Metalloids":
            color='#D55E00'
        elif elem.series == "Halogens":
            color='#CC79A7'
        elif elem.series == "Poor metals":
            color='#56B4E9'
        elif elem.series == "Transition metals":
            color='#009E73'
        elif elem.series == "Lanthanides":
            color='#F0E442'
        elif elem.series == "Actinides":
            color='#0072B2'
        else:
            raise NameError()

        plt.figure(0)
        plt.plot(elem.atomic_number, rho, marker=marker, color=color)
        plt.gca().add_artist(plt.legend(
            (Line2D([0],[0],marker="s",ls="None",c='k', lw=1),Line2D([0],[0],marker="o",ls="None",c='k', lw=1),Line2D([0],[0],marker="v",ls="None",c='k', lw=1)),
            ("Gaz","Liquide","Solide"),
            loc=1, fontsize=8))

        plt.gca().add_artist(plt.legend((
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#348ABD'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#A60628'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#7A68A6'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#467821'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#D55E00'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#CC79A7'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#56B4E9'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#009E73'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#F0E442'),
                                    Line2D([0],[0],marker="None",ls="-",lw=4,color='#0072B2')),
                                    ("Non-métaux",
                                    "Gaz nobles",
                                    "Métaux alcalins",
                                    "Métaux alcalino-terreux",
                                    "Métalloïdes",
                                    "Halogènes",
                                    "Métaux pauvres",
                                    "Métaux de transition",
                                    "Lanthanides",
                                    "Actinides"),
                                    loc=2, ncol=2, fontsize=8))

    except TypeError:
        pass


plt.figure(0)
plt.xlabel("$Z$")
plt.ylabel(r"$\rho$ [$g/cm^3$]")
# plt.yscale("log")
plt.xlim(0, 100)
plt.ylim(0, 25)
plt.axvline(6, color="k", linestyle="--")
plt.text(6, 25.5, "C")
plt.axvline(13, color="k", linestyle="--")
plt.text(13, 25.5, "Al")
plt.axvline(29, color="k", linestyle="--")
plt.text(29, 25.5, "Cu")
plt.axvline(47, color="k", linestyle="--")
plt.text(47, 25.5, "Ag")
plt.axvline(78, color="k", linestyle="--")
plt.text(78, 25.5, "Pt")
#plt.axvline(79, color="k", linestyle="--")
#plt.text(76, 25.5, "Au")
#plt.axvline(82, color="k", linestyle="--")
#plt.text(82, 25.5, "Pb")

#plt.axhline(9, color="k", linestyle="-", lw=1)
#plt.axhline(12, color="k", linestyle="-", lw=1)
#plt.text(101, 16, r"$9-12$ $g/cm^3$", rotation=90)

plt.savefig("rho_Z.png")


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
rcParams['figure.figsize'] = [9.5, 5.10]
rcParams['mathtext.default']='regular'
rcParams['font.size']=16.0
rcParams['figure.subplot.bottom'] = 0.15
rcParams['figure.subplot.left'] = 0.15

from matplotlib.lines import Line2D

# https://www.physics.nist.gov/cgi-bin/Star/compos.pl

# Color for metal, metaloid, ... and marker shape for solid, liquid, gaz in STP

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
        plt.plot(elem.atomic_number, ne, marker=marker, color=color)
        plt.gca().add_artist(plt.legend(
            (Line2D([0],[0],marker="s",ls="None",c='k', lw=1),Line2D([0],[0],marker="o",ls="None",c='k', lw=1),Line2D([0],[0],marker="v",ls="None",c='k', lw=1)),
            ("Gaz","Liquide","Solide"),
            loc=4, fontsize=8))

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
                                    loc=8, ncol=2, fontsize=8))

    except TypeError:
        pass


plt.figure(0)
plt.xlabel("$Z$")
plt.ylabel(r"$n_e$ [$cm^{-3}$]")
plt.yscale("log")
plt.xlim(0, 100)
plt.ylim(1e19, 1e25)
plt.axhline(1.1e21, linestyle="--", color="k")
a=plt.twinx()
a.set_yscale("log")
a.set_ylim(1e19/1.1e21, 1e25/1.1e21)
a.set_ylabel("$n_e$ [$n_c$]")

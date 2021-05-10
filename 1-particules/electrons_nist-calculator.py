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

from star import electron as estar


# Affiche les pouvoirs d'arrêt des matériaux choisis
elements = ["Amorphous_Carbon", "Aluminum", "Copper", "Silver", "Platinum"]
Z = [6, 13, 29, 47, 78]
for i, elem in enumerate(elements):
    data = estar.calculate_stopping_power(eval("estar.PredefinedMaterials."+elem.upper()))

    plt.figure(i)
    plt.plot(data["energy"], data["stopping_power_collision_delta"], label="Collisonnel", color="#A60628", linestyle="--", linewidth=2)
    plt.plot(data["energy"], data["stopping_power_radiative"], label="Radiatif", color="#348ABD", linestyle='-.', linewidth=2)
    plt.plot(data["energy"], data["stopping_power_total"], color="k", linewidth=3)

    plt.gca().add_artist(plt.legend(loc=4))
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$E_e$ [$MeV$]")
    plt.ylabel(r"Pouvoir d'arrêt [$MeV ~ cm^2/g$]")
    plt.xlim(1e-2, 1e3)
    plt.ylim(1e-3, 1e3)
    plt.gca().add_artist(plt.legend((Line2D([0],[0],marker="None",ls="-",c='k', lw=3),), ("Total",), loc=2))
    plt.title("Z = {}".format(Z[i]))
    
    plt.savefig("electrons_Z{:d}.png".format(Z[i]))

# Affiche les pouvoirs d'arrêt en fonction du numéro atomique
elements = [
    "Hydrogen","Helium","Lithium","Beryllium","Boron","Amorphous_Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium",
    "Magnesium","Aluminum","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium",
    "Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium",
    "Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum",
    "Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine",
    "Xenon","Cesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium",
    "Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantalum",
    "Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium",
    "Astatine","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium",
    "Americium","Curium","Berkelium","Californium"]
Z = range(1,99)

energy = np.array([1.00E-02, 1.25E-02,
                    1.50E-02, 1.75E-02, 2.00E-02, 2.50E-02, 3.00E-02, 3.50E-02,
                    4.00E-02, 4.50E-02, 5.00E-02, 5.50E-02, 6.00E-02, 7.00E-02,
                    8.00E-02, 9.00E-02, 1.00E-01, 1.25E-01, 1.50E-01, 1.75E-01,
                    2.00E-01, 2.50E-01, 3.00E-01, 3.50E-01, 4.00E-01, 4.50E-01,
                    5.00E-01, 5.50E-01, 6.00E-01, 7.00E-01, 8.00E-01, 9.00E-01,
                    1.00E+00, 1.25E+00, 1.50E+00, 1.75E+00, 2.00E+00, 2.50E+00,
                    3.00E+00, 3.50E+00, 4.00E+00, 4.50E+00, 5.00E+00, 5.50E+00,
                    6.00E+00, 7.00E+00, 8.00E+00, 9.00E+00, 1.00E+01, 1.25E+01,
                    1.50E+01, 1.75E+01, 2.00E+01, 2.50E+01, 3.00E+01, 3.50E+01,
                    4.00E+01, 4.50E+01, 5.00E+01, 5.50E+01, 6.00E+01, 7.00E+01,
                    8.00E+01, 9.00E+01, 1.00E+02, 1.25E+02, 1.50E+02, 1.75E+02,
                    2.00E+02, 2.50E+02, 3.00E+02, 3.50E+02, 4.00E+02, 4.50E+02,
                    5.00E+02, 5.50E+02, 6.00E+02, 7.00E+02, 8.00E+02, 9.00E+02,
                    1.00E+03])

gZ, gE = np.meshgrid(Z, energy, indexing='ij')

# Initialise les listes de valeurs de pouvoirs d'arrêt, et les listes de transition entre le régime collisionel et radiatif
collisional, radiative, total = [], [], []

collisional_radiative_transition = []

# Récupère les pouvoir d'arrêt + les transitions pour chaque matériau
for i, elem in enumerate(elements):
    data = estar.calculate_stopping_power(eval("estar.PredefinedMaterials."+elem.upper()), energy)

    collisional.append(data["stopping_power_collision_delta"])
    radiative.append(data["stopping_power_radiative"])
    total.append(data["stopping_power_total"])

    collisional_radiative_transition.append(min(energy[data["stopping_power_collision_delta"]<data["stopping_power_radiative"]]))
    
# Affiche les résultats
plt.figure(6, figsize=(8.27, 11.67))
plt.subplots_adjust(bottom=0., top=0.9, wspace=0., hspace=0.)

levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.3, 1.7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
plt.pcolormesh(gZ, gE, total, norm=LogNorm())
plt.colorbar(orientation="horizontal", label=r"Pouvoir d'arrêt total [$MeV ~ cm^2/g$]")
plt.clabel(plt.contour(gZ, gE, total, norm=LogNorm(), levels=levels, colors="k", linewidths=1), levels ,fmt="%.3g", fontsize=8)
plt.yscale("log")
plt.xlabel(r"$Z$")
plt.ylabel(r"$E_e$ [$MeV$]")
plt.ylim(1e-2, 1e3)

plt.plot(Z, collisional_radiative_transition, color="#A60628", linewidth=3)

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

plt.text(101, 10, "Radiatif domine", rotation=90, color="#348ABD")
plt.text(101, 4e-2, "Collisionnel domine", rotation=90, color="#A60628")

plt.savefig("electrons_E_Z.png")

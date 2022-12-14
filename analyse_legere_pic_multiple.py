"""
------------------------------------------------------------------------------

Pour vous faciliter la vie, vous pouvez utiliser le code présent dans le dossier
outils_analyse.

_____________________________________________________________________________
"""
"""
------------------------------------------------------------------------------

Mettres vois import ici

_____________________________________________________________________________
"""

import matplotlib.pyplot as plt
import matplotlib




# Cette ligne contrôle le font size pour les écritures sur le graphique
matplotlib.rcParams.update({'font.size': 18})
"""
------------------------------------------------------------------------------

Lire le fichier des résultats et transformer les valeurs en un array numpy

_____________________________________________________________________________
"""
# Mettre votre code ici








"""
------------------------------------------------------------------------------

Retirer les valeurs qui se trouvent à l'extérieur de l'activation du générateur de rampe.
Ne pas oublier de mettre le début de la rampe comme étant t=0.

_____________________________________________________________________________
"""
# Mettre votre code ici






"""
------------------------------------------------------------------------------

Calculer la pente de la tension du générateur de rampe et son incertitude.
Afficher cette valeur et son incertitude, puis convertir les valeurs de temps
en valeurs de tension.

Ensuite, convertissez les valeurs de tensions du pico en valeur de courant, en considérant que l'échelle
du pico utilisé est de 3nA. 
_____________________________________________________________________________
"""
# Mettre votre code ici




"""
------------------------------------------------------------------------------

Déterminer l'emplacement approximatif des maximums. Ça devrait être
environ: Estimation des pics: [ 1.5860128  3.7164788  6.7701464  8.569206  10.486626  14.676541
 16.499271 ] V

_____________________________________________________________________________
"""
# Mettre votre code ici












# Mettre vos données avec les bonnes unités à la place du None
valeurs_avec_bonnes_unites_determination_des_pics = None  # Array de trois colonnes
liste_des_indexes_des_pics = None  # Liste de nombres entiers

"""
_____________________________________________________________________________
"""
# Ne pas modifier cette section!!!

print("Estimation des pics:", valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 0])

# La figure obtenue devrait correspondre à celle de figures_exemple/estimation_des_pics_multi_pics
plt.figure()
plt.plot(valeurs_avec_bonnes_unites_determination_des_pics[:, 0],
         valeurs_avec_bonnes_unites_determination_des_pics[:, 1],
         label="Courant du pico")
plt.xlabel("Tension entre G1 et le ground [V]")
plt.scatter(valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 0],
            valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 1],
            label="Estimation des pics")
plt.ylabel("Courant mesuré [nA]")
plt.legend()
plt.show()












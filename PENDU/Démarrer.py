import os
import sys
from fonctions import *

demander_pseudo()
afficher_mot_utilisateur()

while(True):
	print("Il vous reste {0} essais !".format(donnees.nombre_de_coups_restants))
	lettre = demander_lettre()
	if not comparer_lettre(lettre):
		afficher_mot_utilisateur()
	else: 
		break




os.system("pause")

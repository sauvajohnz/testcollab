import os
from fonctions import *
from random import randrange

rejouer = True
charger_roulette()

menu()
choix_menu = demander_choix_jeu()

if choix_menu == 1:
	os.system("cls")
	menu_jeu()
	while(rejouer):
		nombre_hasard = randrange(0,50)

		case_mise = demander_case()
		argent_mise = demander_mise()
		calculer_score(case_mise, nombre_hasard, argent_mise)
		demander_rejouer()

else:
	print("erreur de choix de jeu")


os.system("pause")

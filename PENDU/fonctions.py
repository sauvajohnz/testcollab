import os
import donnees
import pickle
import datetime
from random import randrange

lettres_entrees = list()

scores_log = list()

mot_a_trouver = str()
nombre_hasard = randrange(0, len(donnees.liste_mots))
mot_a_trouver = donnees.liste_mots[nombre_hasard]

mot_utilisateur = str()
for mot in mot_a_trouver:
	mot_utilisateur += "*"

def demander_pseudo():
	while(True):
		try:
			pseudo = input("Choisissez un pseudonyme pour cette partie : ")
			if pseudo.find(" ") is not -1:
				print("Il ne faut pas d\'espace dans le pseudonyme")
			elif len(pseudo) > 12:
				print("Votre pseudonyme ne doit pas dépasser 12 caractères")
			elif len(pseudo) < 3:
				print("Votre pseudonyme doit avoir 3 caractères minimum")
			else:
				donnees.pseudonyme = pseudo
				os.system("cls")
				break
		except ValueError:
			print("Le pseudonyme n\'est pas correcte")


def demander_lettre():
	lettre = str()
	while len(lettre) > 1 or not lettre.isalpha():
		try:
			lettre = input("Choissez une lettre : ")
			lettre.lower()
			if len(lettre) > 1 or not lettre.isalpha():
				print("Vous devez choisir une lettre !")
				return demander_lettre()
			else:
				for lettre_deja_entrees in lettres_entrees:
					if lettre == lettre_deja_entrees:
						print("La lettre à déjà été rentrée")
						return demander_lettre()
				lettres_entrees.append(lettre)
				return(lettre)
		except ValueError:
			print("Ce n\'est pas une lettre !")

def comparer_lettre(lettre):
	global mot_utilisateur, mot_a_trouver
	if mot_a_trouver.count(lettre) >= 1:
		os.system("cls")
		print("Il y a {0} fois la lettre {1} dans le mot a trouver".format(mot_a_trouver.count(lettre), lettre))
		while mot_a_trouver.count(lettre) != 0:
			indice = mot_a_trouver.find(lettre)
			mot_utilisateur = mot_utilisateur[:indice] + lettre + mot_utilisateur[indice + 1:] 
			mot_a_trouver = mot_a_trouver[:indice] + "*" + mot_a_trouver[indice + 1:]

			i = len(mot_a_trouver)
			while(i>0):
				test_victoire = str()
				for lettre_ in mot_a_trouver:
					test_victoire += "*"
					i -= 1
				if mot_a_trouver == test_victoire:
					victoire()
					return True
		return False
	else:
		os.system("cls")
		print("Il n'y a pas la lettre {0} dans le mot à trouver.".format(lettre))
		donnees.nombre_de_coups_restants -= 1
		if donnees.nombre_de_coups_restants == 0:
			perdu()
			return True	
		return False

def afficher_mot_utilisateur():
	print(mot_utilisateur)

def victoire():
	os.system("cls")
	print("Vous avez gagné!")
	print("Le mot complet : {0}".format(donnees.liste_mots[nombre_hasard]), end='')
	print("\n\nVotre score a été enregistré ! Vous avez gagné {0} points".format(donnees.nombre_de_coups_restants))
	enregistrer_score()

def perdu():
	os.system("cls")
	print("Vous avez perdu! \nLe mot était {0}".format(donnees.liste_mots[nombre_hasard]))
	enregistrer_score()

def enregistrer_score():
	global scores_log
	if os.path.exists("data/scores.txt"):
		with open("data/scores.txt", "rb") as fichier:
			mon_unpickler = pickle.Unpickler(fichier)
			scores_log = mon_unpickler.load()
	else:
		mon_fichier = open("data/scores.txt", "wb")
		mon_fichier.close()

	with open("data/scores.txt", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		date = avoir_date()
		scores_log.append([donnees.pseudonyme, date, donnees.nombre_de_coups_restants, donnees.liste_mots[nombre_hasard]])
		mon_pickler.dump(scores_log)

def avoir_date():
	ma_date= datetime.datetime.now()
	date = str(ma_date.year)
	date += "-"
	date += str(ma_date.month)
	date += "-"
	date += str(ma_date.day)
	date += " "
	date += str(ma_date.hour)
	date += ":"
	date += str(ma_date.minute)
	return date

if __name__ == "__main__":
	print("Vous ne devez pas lancer ce fichier, lancez Démarrer.py !")
	os.system("pause")
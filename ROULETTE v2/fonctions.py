import datetime
import pickle
import os

nv_joueur = True
argent = 100
nombre_mise = 0
profit = 0
scores_log = []

def charger_roulette():
	global nv_joueur, argent, scores_log

	if os.path.exists("data/donnees.txt"):
		with open("data/donnees.txt", "rb") as fichier:
			mon_depickler = pickle.Unpickler(fichier)

			nv_joueur = mon_depickler.load()
			argent = mon_depickler.load()
			scores_log = mon_depickler.load()
	else:
		sauvegarder_roulette()

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

def sauvegarder_roulette():
	global nv_joueur, nombre_mise, profit, argent
	date = avoir_date()
	scores_log.append([date, nombre_mise, profit, argent])
	with open("data/donnees.txt", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)

		mon_pickler.dump(nv_joueur)
		mon_pickler.dump(argent)
		mon_pickler.dump(scores_log)

def menu_nv_joueur():
	print("Je vois que vous êtes un nouveau joueur, ici l\'argent est sauvegardé \nmême si tu fermes cette fenêtre, mais seulement quand tu décides de quitter\n")
	print("Si tu veux regarder les résultats de tes anciennes parties lance le scripte \n\"Obtenir vos scores\" situé dans le dossier\n")

def menu():
	global nombre_mise, profit, nv_joueur
	if nv_joueur == True:
		menu_nv_joueur()
		demander_choix("Continuer ? (o/n) :")
	nv_joueur = False
	os.system("cls")
	print("*************************************************".center(50))
	print("-MENU-".center(50))
	print("1> Roulette")
	print("2> Pendu (NON DISPONIBLE)\n")
	print("*************************************************".center(50))
def menu_jeu(phrase = ''):
	os.system("cls")
	print("*************************************************".center(50))
	print("-Roulette-".center(50))
	if phrase != '':
		print(phrase)
	if profit > 0:
		print("\nVotre totale de mise sur cette session : ", nombre_mise, " (+", profit, ")", sep='')
	else:
		print("\nVotre totale de mise sur cette session : ", nombre_mise, " (", profit, ")", sep='')
	print("Votre argent : ",argent, "€",sep='')
	print("*************************************************".center(50))

def demander_rejouer():
	choix_utilisateur = str()
	while choix_utilisateur.lower() != "o" and choix_utilisateur.lower() != "n":

		try:
			choix_utilisateur = str(input("Voulez vous rejouer ? (o/n) :"))
			if choix_utilisateur.lower() != "o" and choix_utilisateur.lower() != "n":
				print("Ce n'est pas une réponse attendue !")
			if choix_utilisateur.lower() == "o":
				return True
			elif choix_utilisateur.lower() == "n":
				sauvegarder_roulette()
				print("Aurevoir !")
				os.exit()
		except ValueError:
			print("Vous n\'avez pas tapé de réponse correcte")

def demander_choix(phrase):
	choix_utilisateur = str()
	while choix_utilisateur.lower() != "o" and choix_utilisateur.lower() != "n":
		try:
			choix_utilisateur = str(input(phrase))
			if choix_utilisateur.lower() != "o" and choix_utilisateur.lower() != "n":
				print("Ce n'est pas une réponse attendue !")
			if choix_utilisateur.lower() == "o":
				return True
			elif choix_utilisateur.lower() == "n":
				print("Aurevoir !")
				os.system("quit")
		except ValueError:
			print("Vous n\'avez pas tapé de réponse correcte")

def calculer_score(case_choisi, case_aleatoire, mise):
	global nombre_mise, argent, profit
	nombre_mise += 1
	phrase = "Vous avez misé {1}€ sur la case {0} !.\nLa case tirée au sort est la {2} !\n".format(case_choisi, mise, case_aleatoire)
	if case_choisi == case_aleatoire:
		argent += (mise*3)
		profit += (mise*2)
		menu_jeu(phrase + "\nVous avez choisi le bon nombre ! Vous avez triplé votre mise.")
	elif case_choisi % 2 == 0 and case_aleatoire % 2 == 0:
		argent += (mise*2)
		profit += mise
		menu_jeu(phrase + "\nVotre case et la case tirée aléatoirement sont paires ! \nVous avez gagné le double de votre mise")
	elif case_choisi % 2 != 0 and case_aleatoire % 2 != 0:
		argent += (mise*2)
		profit += mise
		menu_jeu(phrase + "\nVotre case et la case tirée aléatoirement sont impaires ! \nVous avez gagné le double de votre mise")
	else:
		profit -= mise
		menu_jeu(phrase + "\nVous avez perdu votre mise !")


def demander_mise():
	global argent
	choix_utilisateur = -1
	while (choix_utilisateur < 2 or choix_utilisateur > argent):
		try:
			choix_utilisateur = int(input("Nombre d'argent à miser : "))
			if choix_utilisateur < 2:
				print("Vous devez miser au moins 2€ !")
			elif choix_utilisateur > argent:
				print("Vous n\'avez pas assez d\'argent, vous n'avez que ", argent, "€.", sep='')
			if choix_utilisateur >= 2 and choix_utilisateur <= argent:
				argent -= choix_utilisateur
				return choix_utilisateur
		except ValueError:
			print("Vous n\'avez pas tapé de réponse correcte")

def demander_choix_jeu():
	choix_utilisateur = -1
	while (choix_utilisateur <= 0 or choix_utilisateur > 1):
		try:
			choix_utilisateur = int(input("Quel mini-jeu voulez vous choisir? : "))
			if (choix_utilisateur <= 0 or choix_utilisateur > 1):
				print("Cela ne correspond à aucun mini-jeu !")
			if (choix_utilisateur > 0 and choix_utilisateur <= 1):
				return choix_utilisateur
		except ValueError:
			print("Vous n\'avez pas tapé de réponse correcte")

def demander_case():
	choix_utilisateur = -1
	while (choix_utilisateur < 0 or choix_utilisateur > 49):
		try:
			choix_utilisateur = int(input("Numéro de la case à miser : "))
			if (choix_utilisateur < 0 or choix_utilisateur > 49):
				print("Votre case doit être en 0 et 49 !")
			if choix_utilisateur > 0 and choix_utilisateur < 50:
				return choix_utilisateur
		except ValueError:
			print("Vous n\'avez pas tapé de réponse correcte")

if __name__ == "__main__":
	os.system("pause")
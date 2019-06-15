#Jeu de la roulette

import os
from random import randrange
from math import ceil

argent = 100
argent_mise = 0
continuer_jeu = True
tour = 1
confirmation_case = True
confirmation_argent = True
confirmation_rejouer = True

def status_partie():
	print("-                     Tour ",tour,"                  -")
	print("Votre argent: ",argent,"€")


def texte_debut():
	print("------              Jeu de la roulette               -----")
	print("--                        REGLES                        --")
	print("Le principe du jeu est que vous misiez dans un nombre entre")
	print("0 et 49. Un nombre tiré au hasard sera désigné.\nSi le nombre", end='')
	print(" choisi est le même que celui tiré au hasard votre mise est")
	print("multipliée par 3. \nSi votre nombre et celui tiré sont tout deux", end='')
	print(" paire ou impaire vous gagnez votre mise plus 50%. \nSinon vous perdez", end='')
	print(" votre mise.\n\nSi vous avez compris tapez \"compris\"")

texte_debut()

confirmation_debut = str()
while confirmation_debut!="compris":
	try:
		confirmation_debut = str(input())
	except ValueError:
		print("Vous n\'avez pas tapé de chaine de caractère")
	if confirmation_debut=="compris":
		os.system("cls")
	else:
		print("Vous n\'avez pas tapé \"compris\" ! ")

status_partie()

while(continuer_jeu):

	confirmation_argent = True
	confirmation_case = True
	confirmation_rejouer = True

	while(confirmation_argent):
		try:
			argent_mise = int(input("Argent a miser : "))
			if argent_mise > argent:
				print("Vous n'avez pas assez d'argent !")
			elif argent_mise < 2:
				print("Vous devez miser au moins 2€ !")
			else:
				print("Vous avez misé",argent_mise,"€!")
				argent-= argent_mise
				confirmation_argent = False
		except ValueError:
			print("Vous n\'avez pas entré un nombre")


	while(confirmation_case):
		try:
			case_mise = int(input("\nCase à miser (0-49) : "))
			if case_mise >= 0 and case_mise <=49:
				confirmation_case = False
			else:
				print("Ce n\'est pas une case valide !")

		except ValueError:
			print("Vous n\'avez pas entré un nombre")

	tour+=1
	os.system("cls")
	print("-                     Tour ",tour,"                  -")
	print("Vous avez misé sur le",case_mise,"!")
	case_hasard = randrange(0,50)
	print("la case tirée au sort est le", case_hasard, "!\n")
	if case_mise==case_hasard:
		print("Vous avez triplé votre mise !")
		argent+= ceil((argent_mise*3))
	elif case_mise % 2 == 0 and case_hasard % 2 == 0:
		print("Les deux nombres sont paires, vous gagnez 50% de mise en plus !")
		argent+= ceil((argent_mise*1.5))
	elif case_mise % 2 != 0 and case_hasard % 2 != 0: 
		print("Les deux nombres sont impaires, vous gagnez 50% de mise en plus !")
		argent+= ceil((argent_mise*1.5))
	else:
		print("Désolé, vous perdez votre mise")

	print("\nVotre argent: ",argent,"€")

	if argent <= 2:
		while(confirmation_rejouer):
			try:
				rejouer = str(input("\nVoulez vous rejouer ? (oui/non) : "))
				if rejouer == "non":
					continuer_jeu = False
					confirmation_rejouer = False
				elif rejouer == "oui":
					print("Rejouons !")
					os.system("cls")
					tour = 1
					argent = 100
					confirmation_rejouer = False
					status_partie()
				else:
					print("Vous n'avez pas entré une réponse correcte")
			except ValueError:
				print("Ce n'est pas une chaîne de caractère !")

print("\nAurevoir !\n")

os.system("pause")

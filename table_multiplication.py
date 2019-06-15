import os # On importe le module os
import math 

def tirets(nombre_tirets): 
	nombre_tirets = int(nombre_tirets)
	a = 0
	while a < nombre_tirets:
		print("-", end='')
		a+=1

i = 0 # On initialise les variables necessaires au programme
table = input("Table de multiplication : ") #On demande a l utilisateur de remplir les variables
table_limit = input("Limite de nombre a afficher : ")

table = int(table) # On transforme les variables que l utilisateur a remplies en variables de type INT
table_limit = int(table_limit)

table_longueur = math.log10(table) + 1 # On recupere la taille de la table




while i < table_limit : # On calcule en affichant sur la console les resultats
	table_limit_longueur = math.log10(i+1) + 1 # On recupere la taille du facteur
	resultat_longueur = math.log10(table*(i+1)) + 1 # On recupere la taille du resultat
	print("")
	tirets(8+table_longueur+table_limit_longueur+resultat_longueur) # On adapte le nombre de tirets en fonction de la taille de la ligne
	print("\n",table, "x", i+1, " =",table*(i+1)) # On affiche la table et son resultat
	tirets(8+table_longueur+table_limit_longueur+resultat_longueur)
	i+=1 

print("\nFin du programme")

os.system("pause") # On met la console en pause a la fin du programme

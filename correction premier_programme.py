import os # On importe une librairie nommee OS

def traiter_x(x): # On creer une fonction qui traite un nombre selon un certain nombre d'operaitions
	return (x+2)*2

print("Le programme va vous demander de choisir en boucle des valeurs de x")
print("Pour sortir, il suffira de choisir la valeur 0.\n\n")

while(1==1):
	test_valeur = False
	while test_valeur==False:
		try:
			nombre_utilisateur = int(input("Rentrer la valeur de x : ")) # On demande a l'utilisateur de rentrer un nombre dans la variable nombre_utilisateur
			test_valeur = True
		except ValueError:
			print("Erreur dans la valeur de x\n")
			test_valeur = False	

	if nombre_utilisateur==0: # On regarde si l'utilisateur a mis le nombre 0
		break;
	elif nombre_utilisateur>0: # Ou si il a bien respecte la condition de mettre un nombre positif
		print("f("+str(nombre_utilisateur)+") = "+ str(traiter_x(nombre_utilisateur))+ "\n") # On affiche le resultat
	else: # Sinon on en redemande un
		print("Il faut une valeur positive ou nulle !\n")

print("\nFin du programme :)\n\n")

os.system("pause") # On met le programme en pause a sa fin

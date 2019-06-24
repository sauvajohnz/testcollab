import os

def afficher_flotant(nombre):
	if type(nombre) is not float:
		print("Le nombre donné n'est pas un nombre à virgule")
		return 0
	nombre = str(nombre)
	nombre = nombre.split(".")
	print (",".join(nombre))
	

afficher_flotant(1.344)


os.system("pause")
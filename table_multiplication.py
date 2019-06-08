import os # On importe le module os

i = 0 # On initialise les variables nécéssaires au programme
table = input("Table de multiplication : ") #On demande a l'utilisateur de remplir les variables
table_limit = input("Limite de nombre a afficher : ")

table = int(table) # On transforme les variables que l'utilisateur a remplies en variables de type INT
table_limit = int(table_limit)


while i < table_limit : # On calcule en affichant sur la console les résultats
	print(table, "x", i+1, " = ",table*(i+1))
	i+=1

os.system("pause") # On met la console en pause à la fin du programme
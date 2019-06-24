import os

def afficher_list(list):
	for objets in list:
		print(objets)

def echanger_valeurs(list):
	if len(list) <= 1:
		print("La liste n'est pas assez grande")
		return 0
	a = len(list)
	list[a-1], list[0] = list[0], list[a-1]
	return list

def suppression_multiple(list, multiple):
	i = 0
	while i < len(list):
		if list[i] % multiple == 0:
			del list[i]
		else:
			i+=1

L = [15, 3, 4, 6, 9, 8]


suppression_multiple(L, 3)
echanger_valeurs(L)
afficher_list(L)

os.system("pause")
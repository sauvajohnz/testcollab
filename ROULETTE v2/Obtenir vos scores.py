import pickle
import os
 
ma_liste = [1, 2 ,3 ,4]
with open("data/donnees.txt", "rb") as fichier:
	mon_depickler = pickle.Unpickler(fichier)
	lol = mon_depickler.load()
	argent = mon_depickler.load()
	ma_liste = mon_depickler.load()

for i, liste in enumerate(ma_liste):
	print("Le ", ma_liste[i][0], \
	" vous avez joué ", ma_liste[i][1], \
	" fois en faisant ", ma_liste[i][2], \
	"€ de profit. Il vous restait ", ma_liste[i][3], "€.",sep='')

print("\nIl vous reste actuellement ", argent, "€", sep='')


os.system("pause")
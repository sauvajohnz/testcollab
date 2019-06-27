import os
import pickle

scores_log = []

if os.path.exists("data/scores.txt"): 
	with open("data/scores.txt", "rb") as fichier:
		mon_unpickler = pickle.Unpickler(fichier)
		scores_log = mon_unpickler.load()
	for indice, tableau in enumerate(scores_log):
		print("[{0}] Le {1} a gagné {2} points avec le mot {3}".format(scores_log[indice][0], \
																scores_log[indice][1], \
																scores_log[indice][2], \
																scores_log[indice][3] ))
else:
	print("Vous n\'avez pas encore de scores !")

os.system("pause")
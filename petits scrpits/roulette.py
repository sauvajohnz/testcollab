import os
from random import randrange

def choisir(list):
	print (list[randrange(0, len(list))])

jeux = [
	"mathis est pd",
	"kartin est très gentil",
	"alex est pd"
]

choisir(jeux)




os.system("pause")
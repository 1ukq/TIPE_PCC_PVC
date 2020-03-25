from PCC import * #import PCC.py or PCCbis.py

def trouverChemin(l):
	if len(l) <= 1: return ([l])
	listeChemin = []
	for i in range(len(l)):
		lBis = l[:]
		point = lBis.pop(i)
		listeCheminBis = trouverChemin(lBis)
		listeCheminBis = [[point]+chemin for chemin in listeCheminBis]
		listeChemin += listeCheminBis
	return listeChemin

listeChemin = trouverChemin(list(range(1,nbPoint)))
listeChemin = [[0]+chemin+[0] for chemin in listeChemin]

listeCoutChemin = []
for chemin in listeChemin:
	coutChemin = 0
	for i in range(len(chemin)-1):
		coutChemin += matCout[chemin[i]][chemin[i+1]]
	listeCoutChemin += [coutChemin]

coutMin,cheminOptimal = listeCoutChemin[0],listeChemin[0]
for i in range(len(listeCoutChemin)):
	if listeCoutChemin[i] < coutMin:
		coutMin = listeCoutChemin[i]
		cheminOptimal = listeChemin[i]



cheminComplet = [coordPoint[cheminOptimal[0]]]
for i in range(len(cheminOptimal)-1):
	chemin = matChemin[cheminOptimal[i]][cheminOptimal[i+1]]
	cheminComplet += chemin[1:]

for i in range(len(cheminOptimal)-1):
	for x,y in matChemin[cheminOptimal[i]][cheminOptimal[i+1]][1:-1]:
		carte[y][x] = passage


print("PVC - OK\n")

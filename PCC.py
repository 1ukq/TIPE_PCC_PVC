from carte import *
from math import sqrt
import time

###FONCTIONS UTILES
def trouverDistance(coord1,coord2):
	x1,y1 = coord1
	x2,y2 = coord2
	return sqrt((x1-x2)**2+(y1-y2)**2)
	
def trouverDroite(coord1,coord2):
	x1,y1 = coord1
	x2,y2 = coord2
	if x1 != x2:
		a = (y1-y2)/(x1-x2)
		b = y2-x2*a
		def droite(x,y):
			return a * x + b
	else:
		def droite(x,y):
			return y
	return droite
	
def trouverObstacle(coord1,coord2):
	droite = trouverDroite(coord1,coord2)
	x1,y1 = coord1
	x2,y2 = coord2
	add = 0
	if x1 == x2: add = 1
	xMin,xMax = min(x1,x2),max(x1,x2)
	for x in range(xMin,xMax + add): #car list(range(x,x) = []
		b1 = int(droite(x,y1))
		b2 = int(droite(x+1,y2))
		bMin,bMax = min(b1,b2),max(b1,b2)
		for y in range(bMin,bMax+1):
			if typePoint(x,y) == terre:
				return (terre,())
			elif typePoint(x,y) == courant:
				return (courant, carte[y][x])
	return (None,())
	
def trouverCout(coord1,coord2):
	typeObst,caracObst = trouverObstacle(coord1,coord2)
	if typeObst == terre:
		return 0
	elif typeObst == courant:
		return trouverDistance(coord1,coord2)
	return trouverDistance(coord1,coord2)
	
###CREATION DU GRAPHE
coordSommet = coordPoint + coordAccessible
nbSommet = len(coordSommet)

graphe = [[0 for i in range(nbSommet)] for j in range(nbSommet)]

for s1 in range(nbSommet):
	for s2 in range(nbSommet):
		coord1,coord2 = coordSommet[s1],coordSommet[s2]
		graphe[s1][s2] = trouverCout(coord1,coord2)
		graphe[s2][s1] = trouverCout(coord2,coord1) #different car graphe oriente (courants)
		
###ALGORITHME DE DIJKSTRA
def dijkstra(sDepart):
	global graphe,nbSommet
	
	infini = sum(sum(ligne) for ligne in graphe) + 1
	
	sConnu = { sDepart : (0,[sDepart]) }
	sInconnu = { s : (infini,'') for s in range(nbSommet) if s != sDepart }
	
	for sSuivant in range(nbSommet):
		if graphe[sDepart][sSuivant]:
			sInconnu[sSuivant] = [graphe[sDepart][sSuivant],sDepart]
			
	ptTraites = 1 #nombre de points interessants traites
	while sInconnu and ptTraites < nbPoint and any(sInconnu[s][0] < infini for s in sInconnu):
		
		u,uCout = 0,infini
		for k in sInconnu:
			if sInconnu[k][0] < uCout:
				u,uCout = k,sInconnu[k][0]
				
		uCout,uPrec = sInconnu[u]
		for v in sInconnu:
			if graphe[u][v]:
				vCout = uCout + graphe[u][v]
				if vCout < sInconnu[v][0]:
					sInconnu[v] = (vCout,u)
		sConnu[u] = ( uCout, sConnu[uPrec][1] + [u] )
		del sInconnu[u]
		if u < nbPoint: ptTraites += 1
		print(coordSommet[u],ptTraites)
		
	for s in sConnu:
		x,y = coordSommet[s]
		if typePoint(x,y) == accessible:
			carte[y][x] = passage
	
	return sConnu
			
###ALGORITHME DE ASTAR
def aStar(sDepart,sArrivee):
	global graphe,nbSommet,coordSommet 
	
	#creer toutes les matrices heuristiques avant debut algo pour ameliorer complexite temporelle ?
	def heuristique(s):
		return trouverDistance(coordSommet[s],coordSommet[sArrivee])
		
	infini = sum(sum(ligne) for ligne in graphe) + 1
	
	sConnu = { sDepart : (0,[sDepart]) }
	sInconnu = { s : (infini,'') for s in range(nbSommet) if s != sDepart }
	
	for sSuivant in range(nbSommet):
		if graphe[sDepart][sSuivant]:
			sInconnu[sSuivant] = [graphe[sDepart][sSuivant],sDepart]
			
	stop = False
	while sInconnu and not(stop) and any(sInconnu[s][0] < infini for s in sInconnu):
	
		u,uCout = 0,infini
		for k in sInconnu:
			if sInconnu[k][0] + heuristique(k) < uCout + heuristique(u):
				u,uCout = k,sInconnu[k][0]
				print(coordSommet[u])
				
		uCout,uPrec = sInconnu[u]
		for v in sInconnu:
			if graphe[u][v]:
				vCout = uCout + graphe[u][v]
				if vCout < sInconnu[v][0]:
					sInconnu[v] = (vCout,u)
		sConnu[u] = ( uCout, sConnu[uPrec][1] + [u] )
		del sInconnu[u]
		if u == sArrivee: stop = True
		
	for s in sConnu:
		x,y = coordSommet[s]
		if typePoint(x,y) == accessible:
			carte[y][x] = passage
			
	return sConnu
	
	
###PLUS COURT CHEMIN
def PCC(s,sConnu):
	coutTotal,cheminSommet = sConnu[s]
	cheminCoord = [coordSommet[s] for s in cheminSommet]
	return coutTotal,cheminCoord
	
matCout = [[0 for i in range(nbPoint)] for j in range(nbPoint)]
matChemin = [[ [] for i in range(nbPoint)] for j in range(nbPoint)]

if algoPCC == "dijkstra":
	for s1 in range(nbPoint-1):
		sConnu = dijkstra(s1)
		for s2 in range(s1+1,nbPoint):
			print(s1,s2)
			coutChemin,chemin = PCC(s2,sConnu)
			matCout[s1][s2] = coutChemin
			matCout[s2][s1] = coutChemin #car meme cout dans les deux sens
			matChemin[s1][s2] = chemin
			matChemin[s2][s1] = list(reversed(chemin))
elif algoPCC == "aStar":
	for s1 in range(nbPoint-1):
		for s2 in range(s1+1,nbPoint):
			print(s1,s2)
			sConnu = aStar(s1,s2)
			coutChemin,chemin = PCC(s2,sConnu)
			matCout[s1][s2] = coutChemin
			matCout[s2][s1] = coutChemin #car meme cout dans les deux sens
			matChemin[s1][s2] = chemin
			matChemin[s2][s1] = list(reversed(chemin))
			

print("PCC - OK\n")


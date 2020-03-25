from parametres import *
import random as rd

carte = [[eau for i in range(largeurCarte)] for j in range(hauteurCarte)]


def dansFen(x,y):
	return (x>=0 and x<largeurCarte) and (y>=0 and y<hauteurCarte)

def typePoint(x,y):
	if dansFen(x,y):
		if type(carte[y][x]) == tuple:
			return courant
		return carte[y][x]

###PLACEMENT DES TERRES
coordInitIle = [(rd.randint(0,hauteurCarte-1),rd.randint(0,largeurCarte-1)) for i in range(nbIle)]

moinsProb = 1-probAppTerre

for x,y in coordInitIle:
	carte[y][x] = terre

def creaIle(coord,prob):
	global coordTerre
	if prob > 0:
		x,y = coord
		for i in range(-1,2):
			for j in range(-1,2):
				if typePoint(x+i,y+j) == eau and rd.random() < prob:
					creaIle((x+i,y+j),prob-moinsProb)
					carte[y+j][x+i] = terre

for coord in coordInitIle:
	creaIle(coord,probAppTerre)

###PLACEMENT DES POINTS
coordPoint = []

for i in range(nbPoint):
	x,y = rd.randint(0,hauteurCarte-1),rd.randint(0,largeurCarte-1)
	while typePoint(x,y) != eau:
		x,y = rd.randint(0,hauteurCarte-1),rd.randint(0,largeurCarte-1)
	coordPoint += [(x,y)]

x,y = coordPoint[0]
carte[y][x] = bateau

for x,y in coordPoint[1:]:
	carte[y][x] = port

###PLACEMENT DES COURANTS
coordInitCourant = [((rd.randint(0,hauteurCarte-1),rd.randint(0,largeurCarte-1)),(rd.randint(-5,5),rd.randint(-5,5))) for i in range(nbCourant)]

moinsProb = 1-probAppCourant

for (x,y),vect in coordInitCourant:
	carte[y][x] = vect

def creaCourant(coord,prob,vect):
	if prob > 0:
		x,y = coord
		for i in range(-1,2):
			for j in range(-1,2):
				if typePoint(x+i,y+j) == eau and rd.random() < prob:
					newVect = vect[0]+2*rd.random()-1, vect[1]+2*rd.random()-1
					carte[y+j][x+i] = newVect
					creaCourant((x+i,y+j),prob-moinsProb,newVect)

for coord,vect in coordInitCourant:
	creaCourant(coord,probAppCourant,vect)

###COORDONNEES ACCESSIBLES
coordAccessible = []

for x in range(largeurCarte):
	for y in range(hauteurCarte):
		if typePoint(x,y) == terre or typePoint(x,y) == courant:
			for i in range(-1,2):
				for j in range(-1,2):
					if typePoint(x+i,y+j) == eau:
						carte[y+j][x+i] = accessible
						coordAccessible += [(x+i,y+j)]
					elif typePoint(x,y) == courant:
						coordAccessible += [(x+i,y+j)]

coordAccessible = list(set(coordAccessible))

print("carte - OK\n")

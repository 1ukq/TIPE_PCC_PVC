from PVC import *
import tkinter as tk

def afficherCarte():
	largeurCanvas = largeurCarte * pas
	hauteurCanvas = hauteurCarte * pas
	
	def afficherCourant(coord,vect):
		x,y = coord
		vx,vy = vect
		normeVect = (vx*vx + vy*vy)**0.5
		if normeVect == 0:
			normeVect = 1
		can.create_line((x+0.5)*pas, (y+0.5)*pas, ((x+0.5)+vx/(2*normeVect))*pas, ((y+0.5)+vy/(2*normeVect))*pas, arrow = tk.LAST, fill = 'blue')
	#pb d'affichage non centre
	
	def trouverCouleur(x,y):
		t = typePoint(x,y)
		if t == courant:
			return couleur[accessible]
		return couleur[t]
		
	def pointeur(event):
		chaine.configure(text="("+str(event.x//pas)+" , "+str(event.y//pas)+")")
		
	def carre(x, y, couleur):
		can.create_rectangle(x, y, x + pas, y + pas, fill = couleur, outline = couleur)
		
	fen = tk.Tk()
	can = tk.Canvas(fen, width = largeurCanvas, height = hauteurCanvas)
	can.pack()
	can.bind("<Button-1>", pointeur)
	chaine = tk.Label(fen)
	chaine.pack()
	
	for y in range(hauteurCarte):
		for x in range(largeurCarte):
			carre(x*pas, y*pas, trouverCouleur(x, y))
			if typePoint(x,y) == courant:
				vect = carte[y][x]
				afficherCourant((x,y),vect)
				
	for s1 in range(nbPoint):
		for s2 in range(s1+1,nbPoint):
			chemin = matChemin[s1][s2]
			for i in range(len(chemin)-1):
				x1,y1 = chemin[i]
				x2,y2 = chemin[i+1]
				can.create_line((x1+0.5)*pas, (y1+0.5)*pas, (x2+0.5)*pas, (y2+0.5)*pas, fill = 'dim gray', dash = (6,5))
				
	for i in range(len(cheminComplet) -1):
		x1,y1 = cheminComplet[i]
		x2,y2 = cheminComplet[i+1]
		can.create_line((x1+0.5)*pas, (y1+0.5)*pas, (x2+0.5)*pas, (y2+0.5)*pas, fill = 'black')
	
	fen.mainloop()

print("affichage - OK\n")


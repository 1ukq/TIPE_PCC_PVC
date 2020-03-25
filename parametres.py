###CARTE
largeurCarte = 100
hauteurCarte = 100

nbPoint = 6
nbIle = 3
nbCourant = 0

probAppTerre = 0.95
probAppCourant = 0.9

eau = 0
bateau = 1
port = 2
terre = 3
accessible = 4
passage = 5
courant = 6


###AFFICHAGE
pas = 9

condition = [eau,bateau,port,terre,accessible,passage]
couleur = ['cornflower blue', 'tomato', 'gray25', 'sea green', 'SteelBlue1', 'purple1']


###ALGORITHME PLUS COURT CHEMIN
'''algoPCC est "dijkstra" ou "aStar" '''
algoPCC = "dijkstra"

###ALGORITHME PROBLEME DU VOYAGEUR DE COMMERCE

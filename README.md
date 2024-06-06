# SImulation-de-la-propagation-d-un-feu-de-foret
- L'objectif de l'application - Simulation de la propagation d'un feu de foret
On considere que chaque case de l'espace ne peut etre que dans l'un des trois etats suivants: saine(vert),  brulant(rouge), brulee(noir).
On considere deux probabilites p1 et p2. 𝑝1 correspond a la probabilite qu'une case verte voisine d'une case rouge soit contaminee par le feu. 𝑝2 correspond a la probabilite qu'une
case rouge devienne noire a l'instant suivant.On considere pour chaque case rouge la propagation du feu dans les quatre
directions de l'espace. De plus, pour chaque case rouge, on etudie la possibilité qu'elle devienne noire. On considere que la valeur p2 est toujours constante, egale a 0,3. Par contre, la valeur
de vraisemblance p1 peut etre soit constante egale a 0,5*C soit varier en fonction de nombre des cases verts et nouvelles cases rouges.
- Utilisation de l'application
1) En haut a droite on peut obserever la quantite des arbres dans des trois etats possible pour l'instant.
2) En bas a gauche on observe le pourcentage des arbres dans des trois etats possible pour l'instant.
3) En haut a gauche on observe la valeur de vraisemblance p1. Au debut de la simulation, p1 est constante. On appui sur le touche  "fleche gauche <-" pour faire la valeur de p1 changer.
On appui sur le touche  "fleche droite ->" pour faire la valeur de p1 devenir constante.
Le couleur de "vraisemblance p1" interpole entre rouge et violet en fonction des cases noirs presentes sur grille.
4) On observe les courbes des arbres verts, arbres brulants et arbres brulees en fonction d nombre des iterations.
5) On appui sur "fleche haut " pour etre demande si on veut afficher des valeur de vraisemblance p1 et simulation s'arrete.Si on repond "oui" les valeurs sont affichees et la simulation redemarre.
Si on repond un autre chose, la simulation redemarre.
6) On appui sur "fleche bas " pour etre demande si on veut afficher la grille et simulation s'arrete.Si on repond "oui" les valeurs sont affichees et la simulation redemarre.
Si on repond un autre chose, la simulation redemarre.
7) Sur la grille on peut passer la souris dessus pour faire apparaître un feu.
- Les explications -
On fait la structure case avec l'information sur un arbre, la structure grille avec tout des arbres de grille et les autres information sur grille, on fait des procedures pour desinner le grille en fonction
d'etat et pour desinner les nombre des arbres et pourcentage des arbres, ainsi que les fonctions et procedure pour calculer ces nombres. On fait la procedure de la simulation avec les boucles "for" et conditions "if".
On fait main avec initialisation, simulation et les "draw" dans un boucle "while", ainsi que les calculs, affichage de courbe et fonctions de isKeyPressed( ).
- Historique des evolutions
1) 05.04.2024 J'ai fait les strutures, procedure d'initialisation, procedure draw, et commencee a faire procedure de simulation.
2) 12.04.2024 J'ai fait une procedure pour calculer le facteur de propagation, des fonction pour calculer les cases verts, rouges et noirs. J'ai fini une procedure de simulation:
j'ai ajoute un cas d'arret et calculs de facteur de propagation p1. J'ai ajoute le fonctionnement pour que la simulation s'arrete et redemarre si on appui sur les touches fleche bas et fleche haut.
J'ai ajoute une procedure mousePos(x,y) pour pouvoir passer la souris dessus pour faire apparaître un feu.
3) 19.04.2024 J'ai ajoute des courbes, la procedure pour calculer le pourcentage des cases noirs, rouges et verts. L'affichage des valeur de quantite des cases et de pourcentages des cases correspondants sur la grille.
J'ai ajoute la condition pour que la valeur p1 reste constante ou varie si on appui sur les touches fleche droit et fleche gauche. J'ai ajoute les procedures pour afficher la griile et les valeurs de vraisemblance p1.
J'ai ajoute le fonctionnement pour les faire afficher si on appui sur fleche bas ou fleche haut. J'ai ajoute la condition pour que la simulation commence apres 3 sedcondes a partir du demarrage du programme.
J'ai ajoute une umage de foret. J'ai ajoute une procedure d'interpolation des couleurs pour affichage "vraisemblance p1".

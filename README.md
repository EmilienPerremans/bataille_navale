# bataille_navale
Projet python 2T sur un bataille navale

Besoins et fonctionnalités

	On requiert un programme de bataille navale nouvelle génération, basé sur la version classique du jeu et contenant les nouvelles fonctionnalités sous forme de “modes de jeu” apportés par cette version :
 
E : finir la base


-	L+E : Les joueurs interagiront avec le jeu via une interface en ligne de commandes la plus minimaliste possible.

-	L'interaction avec le jeu doit se faire grâce à des commandes écrites dans l’interface, afin que Monsieur Sparrow et les autres joueurs puissent se familiariser avec les commandes en console.

-	
-	E : Le programme proposera un menu permettant de choisir le mode de jeu, une partie solo ou multijoueur, ainsi que de voir l’historique des dernières parties jouées. 
-	L : Cet historique doit être disponible, même après une fermeture du jeu entre deux parties par exemple.
-	L : Les joueurs pourront jouer tout seul (contre l’ordinateur).
-	E : Les joueurs pourront jouer en multijoueur (en 1 vs 1) sur un même poste. Pendant son tour, le joueur 1 ne devra pas être capable de voir ce que le joueur 2 à fait et inversement (l’écran s’effacera entre chaque tour, l’affichage de la grille sera différent en fonction du joueur). Mais dû au partage du poste de jeu, cela reste limité au fair-play de chaque joueur, car rien n’empêche l’un de regarder ce que l’autre fait en direct.
-	L : Une partie doit durer entre 5 et 10 minutes. Pour cela la grille aura une taille maximale limite et les joueurs auront un nombre maximal de bateaux.
-	L + E : Un joueur possède 20 secondes maximum pour réaliser une action lors de son tour, sans quoi celui-ci s’arrête sans que rien ne se passe.
-	L : Afin d’éviter que les parties ne se ressemblent, un aspect/une fonctionnalité aléatoire doit être implémentée.
-	E + L : Le programme doit pouvoir être pris en main par un tiers en vue d’une maintenance à long terme.

Concernant les différents modes de jeu envisagés :

-	E+L : Le mode par défaut (classique) de la bataille navale doit être présent avec une difficulté supplémentaire car notre client, M. Sparrow est trop fort pour le mode normal.
	
-	Le mode revisité de la bataille navale se passe en deux temps : 

La préparation du jeu :
●	E+L : Inclut la possibilité de créer de nouveaux bateaux différents de ceux préexistants (en modifiant leur taille, leur couleur, en y ajoutant un flag, …). 
●	E + L :Cette partie est facultative et peut être skippée dans le cas où le joueur souhaite jouer directement sans créer de nouveaux bateaux.
 
Le cours de la partie :
●	Les parties se jouent avec les règles classiques du jeu à l’exception des ajouts sous-mentionnés.
●	E : Ajout d’une commande de fuite/capitulation, qui fait automatiquement remporter la partie à l’adversaire (ordinateur ou joueur 2).
●	L : Ajout de la possibilité d’un déplacement d’un des navires, équivalent à la valeur de 1 case / tour.
●	Dans le cas où le joueur choisit ce déplacement, il ne peut dès lors pas tirer de torpille et son tour s’arrête.
●	L : En cas de collision lors d’un déplacement avec le bord de la map, le bateau est automatiquement reporté au côté opposé sur celle-ci suivant sa direction à la condition de ne pas être en conflit avec un autre navire déjà positionné à ces positions. Si ce cas se présente, un message d’erreur apparaît indiquant au joueur qu’il ne peut effectuer cette action et doit en réaliser une autre.
●	L’ordinateur ne peut déplacer ses navires en cours de partie.

 

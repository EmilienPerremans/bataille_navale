devinez42
#1880
Python Projet Exam Janvier

devinez42 — 29/11/2022 14:01
ok ok
on s'y mes quand ??
Lucas — 29/11/2022 14:36
tu te sent chaud pour travailler sur quoi?
devinez42 — 29/11/2022 14:55
bah ça serais cool peut être de faire une partie graphique
Lucas — 29/11/2022 15:20
je suis pas sur que ça soit faisable, ou en tout cas j'ai pas prévu de faire ça puisqu'il demande de pouvoir travailler avec des commandes sur console
devinez42 — 29/11/2022 15:24
okay okay pas de problème
Lucas — 29/11/2022 15:35
voici le code actuel
Type de fichier joint : archive
bataille_navale.7z
2.00 MB
Lucas — Hier à 12:55
du coup la je suis en train de travailler sur finaliser le minimum pour qu'on aie un bataille navale 100% fonctionnel et conforme aux regles de bases
est-ce que tu t'es familiarisé avec ce qu'il y a dans le cahier des charges, pour voir s'il y a des trucs qui t'intéressent? 
devinez42 — Hier à 13:08
Alors moi je serais pas contre de travailler sur le mode 2 personnes tu vois ? Et aussi sur des mode spéciaux
Lucas — Hier à 13:13
oki, pour l'instant justement le code est prévu pour 2 joueurs, mais tu pourrais travailler sur ce qui évitera que un joueur puisse voir les bateaux de l'autre etc...
je vais du coup bosser sur le mode 1 joueur
je t'envoie le code asap, j'ai bossé dessus un peu ce matin
je vais voir si j'arrive a faire un git
devinez42 — Hier à 13:42
Donc enfaite MTN les 2 joueurs vois ce que l'autre fait ??
Lucas — Hier à 16:03
yep
voila le code actuellement
import cmd

class InvalidCoordError(Exception):
    pass

class Interface(cmd.Cmd):
    """Simple command processor example."""
    intro = 'Bienvenue dans votre bataille navale, tapez help "commande" ou ? "commande" pour obtenir de l\'aide\n'
    prompt = "jeu"
    def __init__(self, joueurs):
        super().__init__()
        self.joueurs = joueurs
        self.joueur_actuel = joueurs[0]
        self.preparations()

    def changeJoueur(self):
        if self.joueur_actuel == self.joueurs[0]:
            self.joueur_actuel = self.joueurs[1]
        elif self.joueur_actuel == self.joueurs[1]:
            self.joueur_actuel = self.joueurs[0]
        print("%s à vous" %(self.joueur_actuel.nom))

    def preparations(self):
        print(self.joueur_actuel.nom)
        self.prompt = "j1\nplacez vos bateau:"
        if (self.joueurs[1].nbr_bateau == 0):
            print("préparations terminée, joueur1 vous commencez")


    def do_affiche(self,line):
        g.affiche()

    def do_place(self, line):
        l = line.split(" ")
        self.joueur_actuel.place(l[0], l[1])
        self.joueur_actuel.nbr_bateau -= 1 #verifier que le placement est bon
        if self.joueur_actuel.nbr_bateau == 0:
            self.changeJoueur()
            self.preparations()

    def do_tire(self, line):
        self.joueur_actuel.tire(line)
        self.changeJoueur()

    def do_exit(self, line):
        self.do_EOF()
        return True

    def do_EOF(self):
        return True


class Joueur():
    """un joueur qui peut placer des bateau et tirer"""
    def __init__(self, nom, numero):
        self.nom = nom
        self.nbr_bateau = 3
        self.liste_bateau = []
        self.numero = numero

    def place(self,coordA, coordB):
        self.liste_bateau.append(Bateau(coordA, coordB, self))

    def tire(self, case):
        if isinstance(g.cases[case][((self.numero+1)%2)], PartieBateau): #a adapter quand il y aura plus que 2 joueurs
            if g.cases[case][(self.numero%2)].bateau.proprietaire != self:
                g.cases[case][(self.numero%2)].etat = "touché"
                print("touché!")
            else:
                print("c'est ton bateau ça, gamin")
            g.cases[case][(self.numero%2)].bateau.check()
        elif isinstance(g.cases[case][((self.numero+1)%2)], Eau):
            print("plouf!")

class Grille:
    """la grill de jeu qui contiens différents types de cases(eau, parties de bateau, etc"""
    def __init__(self, nombre = 1):
        self.longueur = 10
        self.hauteur = 10
        self.cases = {}
        self.nbr_joueurs = nombre
        for h in range(self.hauteur):
            cle = ""
            for l in range(self.longueur):
                cle = chr(65 + h) + str(l) #cree un string "A1", "A2" etc
                self.cases[cle] = [] #ajoute au dictionaire de cases une case eau avec les coordonées de la case
                for n in range(self.nbr_joueurs):
                    self.cases[cle].append(Eau(cle))

    def affiche(self):
        for e,i in enumerate(self.cases.items()):
            if e % 10 == 0:
                print("\n")
            print(i,end ="")

class Case: #peut etre pas necessaire
    """la forme "brut" d'une case de la grille"""
    def __init__(self,coord):
        self.coord = coord

... (175 lignes restantes)
Réduire
main.py
12 Ko
devinez42 — Hier à 16:39
Okay okay je vais essayer de voir ça
Lucas — Hier à 20:48
@Desirtouan @devinez42 vous savez regarder dans vos évaluations tlca si vous avez un feedback sur le cahier des charges du projet?
devinez42 — Hier à 20:53
Att je vais aller voir
perso je ne le vois pas
@Lucas dit tu veux que je crée moi le git ??
car j'aime encore bien
Lucas — Hier à 20:58
ah, tu sais utiliser git?
Lucas — Hier à 20:58
t'as aussi ça du coup?
Image
devinez42 — Hier à 20:59
plus ou moi je me débrouille oui
c'est quoi le titre stp
Lucas — Hier à 21:00
dans passage d'évaluation
Image
devinez42 — Hier à 21:02
perso j'ai rien de validé moi
hahaha pas cool
je crois s'avoir pq
tu te souviens du petit problème que j'ai eu
bah je me demande si elle n'as pas justement pas compté hahah
bah je le ferais demain matin pour au moins validé ça chez moi
Lucas — Hier à 21:04
ah, merde
devinez42 — Hier à 21:04
ouais je me demande si c'est pas cela le problème
Lucas — Hier à 21:04
ben justement, meme moi il manque des trucs, mais la prof m'a dit que je pouvais me baser sur son feedback, mais j'en ai pas
devinez42 — Hier à 21:05
bah du coup moi j'en ai pas hahaha sorry
je lui demande demain pour ma part
t'es a combien de % ??
SIIIIIIIIIIIIII
merde j'ai un truc
mais j'ai 0 com
tu veux voir le nouveau Cdc que j'ai fais et qu'elle ma validé ??
pour voir les diff ?
Lucas — Hier à 21:09
35
si elle t'as validé "exprimé un besoin client de manière précise", ça m'intéresse yep
devinez42 — Hier à 21:11
va y je t'envoi ça tu serais aussi me partager notre Cdc ??
Type de fichier joint : acrobat
Cahier_des_charges-finalmoyenneCode.pdf
147.70 KB
voila c'est la bazar du projet fictif
Lucas — Hier à 21:12
celui-ci
alz merci
devinez42 — Hier à 21:13
merci à toi je vais aussi vérifier de mon coté et je vais t'envoyer ce que je vais modifier
Lucas — Aujourd’hui à 09:17
PirLucas
lucas_pironet@outlook.fr
devinez42 — Aujourd’hui à 09:19
nice nice l'est go
Lucas — Aujourd’hui à 09:37
https://learngitbranching.js.org/?locale=fr_FR
Learn Git Branching
An interactive Git visualization tool to educate and challenge!
Image
﻿
import cmd

class InvalidCoordError(Exception):
    pass

class Interface(cmd.Cmd):
    """Simple command processor example."""
    intro = 'Bienvenue dans votre bataille navale, tapez help "commande" ou ? "commande" pour obtenir de l\'aide\n'
    prompt = "jeu"
    def __init__(self, joueurs):
        super().__init__()
        self.joueurs = joueurs
        self.joueur_actuel = joueurs[0]
        self.preparations()

    def changeJoueur(self):
        if self.joueur_actuel == self.joueurs[0]:
            self.joueur_actuel = self.joueurs[1]
        elif self.joueur_actuel == self.joueurs[1]:
            self.joueur_actuel = self.joueurs[0]
        print("%s à vous" %(self.joueur_actuel.nom))

    def preparations(self):
        print(self.joueur_actuel.nom)
        self.prompt = "j1\nplacez vos bateau:"
        if (self.joueurs[1].nbr_bateau == 0):
            print("préparations terminée, joueur1 vous commencez")


    def do_affiche(self,line):
        g.affiche()

    def do_place(self, line):
        l = line.split(" ")
        self.joueur_actuel.place(l[0], l[1])
        self.joueur_actuel.nbr_bateau -= 1 #verifier que le placement est bon
        if self.joueur_actuel.nbr_bateau == 0:
            self.changeJoueur()
            self.preparations()

    def do_tire(self, line):
        self.joueur_actuel.tire(line)
        self.changeJoueur()

    def do_exit(self, line):
        self.do_EOF()
        return True

    def do_EOF(self):
        return True


class Joueur():
    """un joueur qui peut placer des bateau et tirer"""
    def __init__(self, nom, numero):
        self.nom = nom
        self.nbr_bateau = 3
        self.liste_bateau = []
        self.numero = numero

    def place(self,coordA, coordB):
        self.liste_bateau.append(Bateau(coordA, coordB, self))

    def tire(self, case):
        if isinstance(g.cases[case][((self.numero+1)%2)], PartieBateau): #a adapter quand il y aura plus que 2 joueurs
            if g.cases[case][(self.numero%2)].bateau.proprietaire != self:
                g.cases[case][(self.numero%2)].etat = "touché"
                print("touché!")
            else:
                print("c'est ton bateau ça, gamin")
            g.cases[case][(self.numero%2)].bateau.check()
        elif isinstance(g.cases[case][((self.numero+1)%2)], Eau):
            print("plouf!")

class Grille:
    """la grill de jeu qui contiens différents types de cases(eau, parties de bateau, etc"""
    def __init__(self, nombre = 1):
        self.longueur = 10
        self.hauteur = 10
        self.cases = {}
        self.nbr_joueurs = nombre
        for h in range(self.hauteur):
            cle = ""
            for l in range(self.longueur):
                cle = chr(65 + h) + str(l) #cree un string "A1", "A2" etc
                self.cases[cle] = [] #ajoute au dictionaire de cases une case eau avec les coordonées de la case
                for n in range(self.nbr_joueurs):
                    self.cases[cle].append(Eau(cle))

    def affiche(self):
        for e,i in enumerate(self.cases.items()):
            if e % 10 == 0:
                print("\n")
            print(i,end ="")

class Case: #peut etre pas necessaire
    """la forme "brut" d'une case de la grille"""
    def __init__(self,coord):
        self.coord = coord

class Eau(Case):
    """une case de la grille avec juste de l'eau"""
    def __init__(self, coord):
        super().__init__(coord)
        self.type = "eau"

    def __repr__(self):
        return self.type

class PartieBateau(Case):
    """une case de la grille avec partie de bateau"""
    def __init__(self, coord, bateau):
        super().__init__(coord)
        self.bateau = bateau
        self.type = "partie bateau"
        self.etat = "indemne"

    def __repr__(self):
        return self.type + " " + self.bateau.proprietaire.nom  + " " + self.etat

class Bateau():
    """un bateau, composé de plusieurs parties qui se positionne dans la grille et vérifie son état apres chaque coup"""
    def __init__(self, coordA, coordB, proprietaire):
        #self.longueur = longueur
        if coordA not in g.cases.keys():
            raise InvalidCoordError("Coord not in grid")
        self.coordA = coordA
        if coordB not in g.cases.keys():
            raise InvalidCoordError("Coord not in grid")
        self.coordB = coordB
        #self.direction = direction
        self.proprietaire = proprietaire
        self.liste_parties = []
        self.placement2()

    def placement2(self):
        if self.coordA[0] == self.coordB[0]:#bateau horizontal
            for i in range(abs(int(self.coordA[1])-int(self.coordB[1]))+1):#boucle autand de fois qu'il n'y a de parties de bateau
                if (int(self.coordA[1])-int(self.coordB[1])) < 0: #si le bateau vas de gauche a droite
                    coord = self.coordA[0] + str(int((self.coordA[1])) + i)
                else:
                    coord = self.coordA[0] + str(int((self.coordA[1])) - i)
                if (g.cases[coord][((self.proprietaire.numero+1)%2)].type != "eau"):#si la case ou on veux placer un bateau n'est pas vide
                    print("vous ne pouvez pas placer un bateau sur un autre bateau")
                    self.liste_parties = []
                    return
                self.liste_parties.append(coord)#la liste des parties du bateau se complete

            #verification en cas de bateau adgacent (lambda?)
            for b in self.proprietaire.liste_bateau:
                p1 = b.liste_parties
                p2 = self.liste_parties

                ordP1PlusOne = list(map(lambda x: x[0] + str(int(x[1]) + 1), p1))
                ordP1MinusOne = list(map(lambda x: x[0] + str(int(x[1]) - 1), p1))

                absP1PlusOne = list(map(lambda x: chr(ord(x[0]) + 1) + x[1], p1))
                absP1MinusOne = list(map(lambda x: chr(ord(x[0]) - 1) + x[1], p1))

                if (any(x in p1 for x in p2) or any(x in ordP1PlusOne for x in p2) or any(
                        x in ordP1MinusOne for x in p2) or any(x in p1 for x in p2) or any(
                        x in absP1PlusOne for x in p2) or any(x in absP1MinusOne for x in p2)):
                    self.liste_parties = []
                    print("Le bateau est à coté d'un autre")
                    return


            for c in self.liste_parties: #la liste des parties du bateau est complete, mais il n'y a pas encore d'instances dans la grille
                g.cases[c][((self.proprietaire.numero+1)%2)] = PartieBateau(c, self)

        elif self.coordA[1] == self.coordB[1]:#bateau horizontal
            for i in range(abs(ord(self.coordA[0])-ord(self.coordB[0]))+1):
                if (ord(self.coordA[0])-ord(self.coordB[0])) < 0:
                    coord = chr(ord(self.coordA[0]) + i) + self.coordA[1]
                else:
                    coord = chr(ord(self.coordA[0]) - i) + self.coordA[1]
                if (g.cases[coord][((self.proprietaire.numero+1)%2)].type != "Eau"):
                    print("vous ne pouvez pas placer un bateau sur un autre bateau")
                    self.liste_parties = []
                    return
                self.liste_parties.append(coord)

            for b in self.proprietaire.liste_bateau:
                p1 = b.liste_parties
                p2 = self.liste_parties

                ordP1PlusOne = list(map(lambda x: x[0] + str(int(x[1]) + 1), p1))
                ordP1MinusOne = list(map(lambda x: x[0] + str(int(x[1]) - 1), p1))

                absP1PlusOne = list(map(lambda x: chr(ord(x[0]) + 1) + x[1], p1))
                absP1MinusOne = list(map(lambda x: chr(ord(x[0]) - 1) + x[1], p1))

                if (any(x in p1 for x in p2) or any(x in ordP1PlusOne for x in p2) or any(
                        x in ordP1MinusOne for x in p2) or any(x in p1 for x in p2) or any(
                    x in absP1PlusOne for x in p2) or any(x in absP1MinusOne for x in p2)):
                    self.liste_parties = []
                    print("Le bateau est à coté d'un autre")
                    return

            for c in self.liste_parties:
                g.cases[c][((self.proprietaire.numero+1)%2)] = PartieBateau(c, self)
        else:
            print("veuillez entrer des coordonnées valides")
    """
    def placement(self):
        #place le bateau sur la grille
        if self.direction == "droite":
            for l in range(self.longueur):
                coord = self.coord[0] + str(int((self.coord[1]))+l)
                self.liste_parties.append(coord)
                if all(c in g.cases.keys() for c in self.liste_parties):
                    g.cases[coord] = PartieBateau(coord, self)
                else:
                    print("bateau en dehors du terrain")
                    break

        if self.direction == "gauche":
            for l in range(self.longueur):
                coord = self.coord[0] + str(int((self.coord[1]))-l)
                self.liste_parties.append(coord)
                if all(c in g.cases.keys() for c in self.liste_parties):
                    g.cases[coord] = PartieBateau(coord, self)
                else:
                    print("bateau en dehors du terrain")
                    break
        elif self.direction == "bas":
            for l in range(self.longueur):
                coord = chr(ord(self.coord[0])+l) + self.coord[1]
                self.liste_parties.append(coord)
                if all(c in g.cases.keys() for c in self.liste_parties):
                    g.cases[coord] = PartieBateau(coord, self)
                else:
                    print("bateau en dehors du terrain")
                    break
        elif self.direction == "haut":
            for l in range(self.longueur):
                coord = chr(ord(self.coord[0])-l) + self.coord[1]
                self.liste_parties.append(coord)
                if all(c in g.cases.keys() for c in self.liste_parties):
                    g.cases[coord] = PartieBateau(coord, self)
                else:
                    print("bateau en dehors du terrain")
                    break
    """
    def check(self):
        etatsParties = []
        for c in self.liste_parties:
            etatsParties.append(g.cases[c][((self.proprietaire.numero+1)%2)].etat)
        if "indemne" in etatsParties:
            return
        #if "bateau" in *(g.cases(*self.liste_cases):
        #    print("beateau non coulé")
        else:
            for i in range(len(self.liste_parties)):
                g.cases[self.liste_parties[i]][((self.proprietaire.numero+1)%2)].etat = "coulé"
            print("bateau coulé!")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("nom", help="nom des joueurs", nargs="+")
    #parser.add_argument("mode", help="message", choices=["normal", "2.0"])
    l = parser.parse_args()
    g = Grille(len(l.nom))
    j1 = Joueur(l.nom[0],1)
    en = Joueur(l.nom[1],2)
    g.affiche()
    print("\n")
    Interface([j1,en]).cmdloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
main.py
12 Ko

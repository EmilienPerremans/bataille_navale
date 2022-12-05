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

    def default(self, line: str):
        print("commande non reconnue")
        self.do_help("")

    def emptyline(self):
        print("veuillez entrer quelque chose")
        self.do_help("")

    def gameOver(self, perdant):
        print("Fin de partie, %s a perdu" % perdant.nom)

    def changeJoueur(self):
        if self.joueurs[1].nom == "ordi":
            self.joueurs[1].tire()
            print("l'ordi à tiré")
        else:
            if self.joueur_actuel == self.joueurs[0]:
                self.joueur_actuel = self.joueurs[1]
            elif self.joueur_actuel == self.joueurs[1]:
                self.joueur_actuel = self.joueurs[0]
            s = self.joueur_actuel.nom + " a vous: "
            self.prompt = s

    def preparations(self):
        if self.joueurs[1].nom == "ordi":
            s = self.joueur_actuel.nom + "\nplacez vos bateau: "
            self.prompt = s
            if (self.joueurs[0].nbr_bateau == 0):
                self.joueurs[1].place()
                print("L'ordi place ses bateaux...")
                print("préparations terminée, joueur1 vous commencez")
                self.prompt = "j1 a vous: "
        else:
            s = self.joueur_actuel.nom + "\nplacez vos bateau: "
            self.prompt = s
            if (self.joueurs[1].nbr_bateau == 0):
                print("préparations terminée, joueur1 vous commencez")
                self.prompt = "j1 a vous: "

    def do_affiche(self, line):
        g.affiche()

    def help_affiche(self):
        print("affiche la grille")

    def do_place(self, line):
        l = line.split(" ")
        if len(l) != 2:
            print("veuillez entrer deux coordonnées")
            return

        try:
            self.joueur_actuel.place(l[0], l[1])
        except Exception as message:
            print("erreur ligne 55")
            print("details de l'erreur:", message)
        else:
            self.joueur_actuel.nbr_bateau -= 1  # verifier que le placement est bon
            if self.joueur_actuel.nbr_bateau == 0:
                if self.joueurs[1].nom != "ordi":
                    self.changeJoueur()
                self.preparations()

    def do_tire(self, line):
        if self.joueur_actuel.nbr_bateau != 0:
            print("il vous reste des bateaux à placer")
            return
        try:
            self.joueur_actuel.tire(line)
        except Exception as message:
            print("erreur ligne 65")
            print("details de l'erreur:", message)
        else:
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

    def place(self, coordA, coordB):
        for o in self.liste_bateau:
            print(o.liste_parties)
        self.liste_bateau.append(Bateau(coordA, coordB, self))

    def tire(self, case):
        if isinstance(g.cases[case][((self.numero) % 2)],
                      PartieBateau):  # a adapter quand il y aura plus que 2 joueurs
            if g.cases[case][(self.numero % 2)].bateau.proprietaire != self:
                g.cases[case][(self.numero % 2)].etat = "touché"
                print("touché!")
            else:
                print("c'est ton bateau ça, gamin")
            g.cases[case][(self.numero % 2)].bateau.check()
        elif isinstance(g.cases[case][((self.numero) % 2)], Eau):
            g.cases[case][(self.numero % 2)].etat = "touché"
            print("plouf!")


class Ordinateur(Joueur):
    """Joueur entièrement geré par l'ordinateur"""

    def __init__(self, nom, numero):
        super().__init__(nom, numero)

    def place(self):
        coordA = "A1"  # aléatoiriser
        coordB = "A2"
        for o in self.liste_bateau:
            print(o.liste_parties)
        self.liste_bateau.append(Bateau(coordA, coordB, self))

    def tire(self):
        case = "A1"  # randomiser
        if isinstance(g.cases[case][((self.numero) % 2)],
                      PartieBateau):  # a adapter quand il y aura plus que 2 joueurs
            if g.cases[case][(self.numero % 2)].bateau.proprietaire != self:
                g.cases[case][(self.numero % 2)].etat = "touché"
                print("touché!")
            else:
                print("c'est ton bateau ça, gamin")
            g.cases[case][(self.numero % 2)].bateau.check()
        elif isinstance(g.cases[case][((self.numero) % 2)], Eau):
            g.cases[case][(self.numero % 2)].etat = "touché"
            print("plouf!")


class Grille:
    """la grill de jeu qui contiens différents types de cases(eau, parties de bateau, etc"""

    def __init__(self, nombre=1):
        self.longueur = 10
        self.hauteur = 10
        self.cases = {}
        self.nbr_joueurs = nombre
        for h in range(self.hauteur):
            cle = ""
            for l in range(self.longueur):
                cle = chr(65 + h) + str(l)  # cree un string "A1", "A2" etc
                self.cases[cle] = []  # ajoute au dictionaire de cases une case eau avec les coordonées de la case
                for n in range(self.nbr_joueurs):
                    self.cases[cle].append(Eau(cle))

    def affiche(self):
        for e, i in enumerate(self.cases.items()):
            separrateur = "  "
            affichA = []
            affichB = []
            affichC = []
            affichD = []
            affichE = []
            affichF = []
            affichG = []
            affichH = []
            affichI = []
            affichJ = []
            self.toutesLesCase = []

            for e, i in enumerate(self.cases.items()):
                if i[0][0] == 'A':
                    affichA.append(i[0])
                    self.toutesLesCase.append(affichA)
                elif i[0][0] == 'B':
                    affichB.append(i[0])
                    self.toutesLesCase.append(affichB)
                elif i[0][0] == 'C':
                    affichC.append(i[0])
                    self.toutesLesCase.append(affichC)
                elif i[0][0] == 'D':
                    affichD.append(i[0])
                    self.toutesLesCase.append(affichD)
                elif i[0][0] == 'E':
                    affichE.append(i[0])
                    self.toutesLesCase.append(affichE)
                elif i[0][0] == 'F':
                    affichF.append(i[0])
                    self.toutesLesCase.append(affichF)
                elif i[0][0] == 'G':
                    affichG.append(i[0])
                    self.toutesLesCase.append(affichG)
                elif i[0][0] == 'H':
                    affichH.append(i[0])
                    self.toutesLesCase.append(affichH)
                elif i[0][0] == 'I':
                    affichI.append(i[0])
                    self.toutesLesCase.append(affichI)
                elif i[0][0] == 'J':
                    affichJ.append(i[0])
                    self.toutesLesCase.append(affichJ)
            # Sert à l'affichage en interface graphique
        fenetre = Tk()
        canvas = Canvas(fenetre, width=390, height=220, background='yellow')
        txtA = canvas.create_text(200, 20, text=separrateur.join(affichA), font="TkFixedFont", fill="blue")
        txtB = canvas.create_text(200, 40, text=separrateur.join(affichB), font="TkFixedFont", fill="blue")
        txtC = canvas.create_text(200, 60, text=separrateur.join(affichC), font="TkFixedFont", fill="blue")
        txtD = canvas.create_text(200, 80, text=separrateur.join(affichD), font="TkFixedFont", fill="blue")
        txtE = canvas.create_text(200, 100, text=separrateur.join(affichE), font="TkFixedFont", fill="blue")
        txtF = canvas.create_text(200, 120, text=separrateur.join(affichF), font="TkFixedFont", fill="blue")
        txtG = canvas.create_text(200, 140, text=separrateur.join(affichG), font="TkFixedFont", fill="blue")
        txtH = canvas.create_text(200, 160, text=separrateur.join(affichH), font="TkFixedFont", fill="blue")
        txtI = canvas.create_text(200, 180, text=separrateur.join(affichI), font="TkFixedFont", fill="blue")
        txtJ = canvas.create_text(200, 200, text=separrateur.join(affichJ), font="TkFixedFont", fill="blue")
        canvas.pack()


class Case:  # peut etre pas necessaire
    """la forme "brut" d'une case de la grille"""

    def __init__(self, coord):
        self.coord = coord


class Eau(Case):
    """une case de la grille avec juste de l'eau"""

    def __init__(self, coord):
        super().__init__(coord)
        self.type = "eau"
        self.etat = "indemne"

    def __repr__(self):
        return self.type + " " + self.etat


class PartieBateau(Case):
    """une case de la grille avec partie de bateau"""

    def __init__(self, coord, bateau):
        super().__init__(coord)
        self.bateau = bateau
        self.type = "partie bateau"
        self.etat = "indemne"

    def __repr__(self):
        return self.type + " " + self.bateau.proprietaire.nom + " " + self.etat


class Bateau():
    """un bateau, composé de plusieurs parties qui se positionne dans la grille et vérifie son état apres chaque coup"""

    def __init__(self, coordA, coordB, proprietaire):
        # self.longueur = longueur
        if coordA not in g.cases.keys():
            raise InvalidCoordError("Coord not in grid")
        self.coordA = coordA
        if coordB not in g.cases.keys():
            raise InvalidCoordError("Coord not in grid")
        self.coordB = coordB
        # self.direction = direction
        self.proprietaire = proprietaire
        self.liste_parties = []
        self.etat = "indemne"
        self.placement2()

    def placement2(self):
        if self.coordA[0] == self.coordB[0]:  # bateau horizontal
            for i in range(abs(int(self.coordA[1]) - int(
                    self.coordB[1])) + 1):  # boucle autand de fois qu'il n'y a de parties de bateau
                if (int(self.coordA[1]) - int(self.coordB[1])) < 0:  # si le bateau vas de gauche a droite
                    coord = self.coordA[0] + str(int((self.coordA[1])) + i)
                else:
                    coord = self.coordA[0] + str(int((self.coordA[1])) - i)
                if (g.cases[coord][((
                                            self.proprietaire.numero + 1) % 2)].type != "eau"):  # si la case ou on veux placer un bateau n'est pas vide
                    self.liste_parties = []
                    raise InvalidCoordError("vous ne pouvez pas placer un bateau sur un autre bateau")
                self.liste_parties.append(coord)  # la liste des parties du bateau se complete

            # verification en cas de bateau adgacent (lambda?)
            for b in self.proprietaire.liste_bateau:
                if b == self:
                    continue
                p1 = b.liste_parties.copy()
                p2 = self.liste_parties.copy()

                ordP1PlusOne = list(map(lambda x: x[0] + str(int(x[1]) + 1), p1))
                ordP1MinusOne = list(map(lambda x: x[0] + str(int(x[1]) - 1), p1))

                absP1PlusOne = list(map(lambda x: chr(ord(x[0]) + 1) + x[1], p1))
                absP1MinusOne = list(map(lambda x: chr(ord(x[0]) - 1) + x[1], p1))

                if (any(x in p1 for x in p2) or any(x in ordP1PlusOne for x in p2) or any(
                        x in ordP1MinusOne for x in p2) or any(x in p1 for x in p2) or any(
                    x in absP1PlusOne for x in p2) or any(x in absP1MinusOne for x in p2)):
                    self.liste_parties = []
                    raise InvalidCoordError("Le bateau est à coté d'un autre")
            print(self.liste_parties)

            for c in self.liste_parties:  # la liste des parties du bateau est complete, mais il n'y a pas encore d'instances dans la grille
                g.cases[c][((self.proprietaire.numero + 1) % 2)] = PartieBateau(c, self)

        elif self.coordA[1] == self.coordB[1]:  # bateau horizontal
            for i in range(abs(ord(self.coordA[0]) - ord(self.coordB[0])) + 1):
                if (ord(self.coordA[0]) - ord(self.coordB[0])) < 0:
                    coord = chr(ord(self.coordA[0]) + i) + self.coordA[1]
                else:
                    coord = chr(ord(self.coordA[0]) - i) + self.coordA[1]
                if g.cases[coord][((self.proprietaire.numero + 1) % 2)].type != "Eau":
                    self.liste_parties = []
                    raise InvalidCoordError("vous ne pouvez pas placer un bateau sur un autre bateau")
                self.liste_parties.append(coord)

            for b in self.proprietaire.liste_bateau:
                if b == self:
                    continue
                p1 = b.liste_parties.copy()
                p2 = self.liste_parties.copy()

                ordP1PlusOne = list(map(lambda x: x[0] + str(int(x[1]) + 1), p1))
                ordP1MinusOne = list(map(lambda x: x[0] + str(int(x[1]) - 1), p1))

                absP1PlusOne = list(map(lambda x: chr(ord(x[0]) + 1) + x[1], p1))
                absP1MinusOne = list(map(lambda x: chr(ord(x[0]) - 1) + x[1], p1))

                if (any(x in p1 for x in p2) or any(x in ordP1PlusOne for x in p2) or any(
                        x in ordP1MinusOne for x in p2) or any(x in p1 for x in p2) or any(
                    x in absP1PlusOne for x in p2) or any(x in absP1MinusOne for x in p2)):
                    self.liste_parties = []
                    raise InvalidCoordError("Le bateau est à coté d'un autre")
            print(self.liste_parties)

            for c in self.liste_parties:
                g.cases[c][((self.proprietaire.numero + 1) % 2)] = PartieBateau(c, self)
        else:
            raise InvalidCoordError("veuillez entrer des coordonnées valides")

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
            etatsParties.append(g.cases[c][((self.proprietaire.numero + 1) % 2)].etat)
        if "indemne" in etatsParties:
            return
        # if "bateau" in *(g.cases(*self.liste_cases):
        #    print("beateau non coulé")
        else:
            for i in range(len(self.liste_parties)):
                g.cases[self.liste_parties[i]][((self.proprietaire.numero + 1) % 2)].etat = "coulé"
            self.etat = "coulé"
            print("bateau coulé!")
            etatBateaux = []
            for b in self.proprietaire.liste_bateau:
                etatBateaux.append(b.etat)
            if not any(x != "coulé" for x in etatBateaux):
                inter.gameOver(self.proprietaire)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("nom", help="nom des joueurs", nargs="+")
    # parser.add_argument("mode", help="message", choices=["normal", "2.0"])
    l = parser.parse_args()
    g = Grille(len(l.nom))
    j1 = Joueur(l.nom[0], 1)
    if (l.nom[1]) == "ordi":
        ordi = Ordinateur("ordi", 2)
        inter = Interface([j1, ordi])
    else:
        en = Joueur(l.nom[1], 2)
        inter = Interface([j1, en])
    g.affiche()
    print("\n")

    inter.cmdloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

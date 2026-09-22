

class Personnage:

    def __init__(self, pseudo:str, niveau=1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau
        self.__pv_max = niveau

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, nv_pseudo):
        if not isinstance(nv_pseudo, str):
            raise TypeError
        self.__pseudo = nv_pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @niveau.setter
    def niveau(self, nv_niveau):
        if not isinstance(nv_niveau, int):
            raise TypeError
        self.__niveau = nv_niveau

    @property
    def pv(self) -> int:
        return self.__pv

    @pv.setter
    def pv(self, nv_pv):
        if nv_pv > getattr(self, '__pv_max', nv_pv):
            self.__pv = self.__pv_max
        elif nv_pv < 0:
            self.__pv = 0
        else:
            self.__pv = nv_pv

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, nv_initiative):
        if not isinstance(nv_initiative, int):
            raise TypeError
        self.__initiative = nv_initiative

    @property
    def pv_max(self) -> int:
        return self.__pv_max

    @pv_max.setter
    def pv_max(self, nv_max):
        if not isinstance(nv_max, int):
            raise TypeError
        self.__pv_max = nv_max



    def _attaque(self, opposant:Personnage):

        if opposant.__initiative > self.__initiative:
            self.__pv -= opposant.degat()

            if self.__pv > 0:
                opposant.__pv -= self.degat()

        elif opposant.__initiative < self.__initiative:
            opposant.__pv -= self.degat()

            if opposant.__pv > 0:
                self.__pv -= opposant.degat()

        else:
            self.__pv -= opposant.degat()
            opposant.__pv -= self.degat()


    def combat(self, opposant:Personnage):

        tour = 1
        while opposant.__pv > 0 and self.__pv > 0:
            print(f"Tour {tour}")
            self._attaque(opposant)
            print(f"{opposant.__pseudo} : {opposant.__pv} | {self.__pseudo} : {self.__pv} PV")
            tour += 1

        if opposant.__pv == 0 and self.__pv == 0:
            print(f"Match nul")

        elif opposant.__pv > 0:
            print(f"Le vainqueur est {opposant.__pseudo} avec {opposant.__pv} PV")

        else:
            print(f"Le vainqueur est {self.__pseudo} avec {self.__pv} PV")


    def soigner(self):
        self.__pv = self.__pv + self.__niveau

    def degat(self):
        return self.__niveau

    def __str__(self):
        return f"{self.pseudo}, Niv {self.niveau}"


    def __eq__(self, opposant):
        if isinstance(opposant, Personnage):
            return self.pseudo == opposant.pseudo
        return False





class Guerrier(Personnage):

    def __init__(self, pseudo:str, niveau=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6
        self.pv_max = niveau * 8 + 4

    def degat(self):
        return self.niveau * 2


class Mage(Personnage):

    def __init__(self, pseudo:str, niveau=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.pv_max = niveau * 5 + 10
        self.__mana = niveau * 5


    def degat(self):

        if self.__mana > 0:
            self.__mana -= 4
            return self.__mana + 3

        else:
            return self.__mana




class Joueur(Personnage):

    def __init__(self, nom:str, max_personnages: int):
        self.__nom = nom
        self.__max_personnages = max_personnages
        self.__personnages = []

    @property
    def personnages(self) -> list:
        return self.__personnages

    @personnages.setter
    def personnages(self, nv_personnages):
        if not isinstance(nv_personnages, list):
            raise TypeError
        self.__personnages = nv_personnages

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nv_nom):
        if not isinstance(nv_nom, str):
            raise TypeError
        self.__nom = nv_nom

    def ajout_perso(self, perso):
        if len(self.__personnages) < self.__max_personnages:
            self.__personnages.append(perso)
            print(f"{perso} ajouté")

        else:
            print(f"Ajout impossible")

    def get_personnage_num(self, numero):
        if 0 <= numero < len(self.__personnages):
            return self.__personnages[numero]
        return None

    def get_personnage_pseudo(self, pseudo):
        for p in self.__personnages:
            if p.pseudo == pseudo:
                return p
        return None

    def get_personnage_perso(self, p_recherche):
        for p in self.__personnages:
            if p == p_recherche:
                return p
        return None


    def eliminer_personnage_numero(self, numero):
        if 0 <= numero < len(self.__personnages):
            p = self.__personnages.pop(numero)
            print(f"Personnage {p.pseudo} éliminé")

    def eliminer_personnage_pseudo(self, pseudo):
        p = self.get_personnage_pseudo(pseudo)
        if p:
            self.__personnages.remove(p)
            print(f"Personnage {pseudo} éliminé")

    def eliminer_personnage_perso(self, p_recherche):
        if p_recherche in self.__personnages:
            self.__personnages.remove(p_recherche)
            print(f"Personnage {p_recherche.pseudo} éliminé")


if __name__ == "__main__":
    # Combat
    chevalier = Guerrier("Gregos le chevalier", 15)
    sorcier = Mage("Patpat", 15)
    chevalier.combat(sorcier)

    # Soins
    print(f"\nPV de {chevalier.pseudo} après le combat : {chevalier.pv}")
    chevalier.soigner()
    print(f"PV de {chevalier.pseudo} après un soin {chevalier.niveau} PV : {chevalier.pv}")

    joueur1 = Joueur("Joueur 1", 2)
    joueur2 = Joueur("Joueur 2", 3)

    p1 = Guerrier("Garen", 10)
    p2 = Mage("Ryze", 10)
    p3 = Personnage("Paysan", 1)

    joueur1.ajout_perso(p1)
    joueur1.ajout_perso(p2)
    joueur1.ajout_perso(p3)

    joueur2.ajout_perso(p3)

    print("\nSuppression d'un personnage :")
    joueur1.eliminer_personnage_pseudo("Garen")


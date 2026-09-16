from statistics import pvariance


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
            self.__pv -=opposant.__niveau

            if self.__pv > 0:
                opposant.__pv -= self.__niveau

        elif opposant.__initiative < self.__initiative:
            opposant.__pv -= self.__niveau

            if opposant.__pv > 0:
                self.__pv -= opposant.__niveau

        else:
            self.__pv -=opposant.__niveau
            opposant.__pv -=self.__niveau


    def combat(self, opposant:Personnage):

        tour = 1
        while opposant.__pv > 0 or self.__pv > 0:
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







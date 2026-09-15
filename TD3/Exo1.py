import math


def division(value1, value2):
    return value1 / value2






class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valeur):

        if not isinstance(valeur, (int, float)):
            raise TypeError("La coordonnée x doit être un nombre")

        self.__x = float(valeur)





    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valeur):

        if not isinstance(valeur, (int, float)):
            raise TypeError("La coordonnée y doit être un nombre")
        self.__y = float(valeur)





    def distanceCoord(self, a, b):
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)


class Cercle:

    def __init__(self, rayon, centre=None):
        if centre is None:
            self.centre = Point()
        else:
            self.centre = centre

        self.rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, valeur):

        if not isinstance(valeur, (int, float)):
            raise TypeError("Le rayon doit être un nombre")

        if valeur < 0:
            raise ValueError("Le rayon ne peut pas être négatif")

        self.__rayon = float(valeur)



if __name__ == "__main__":
    try:
        print(division(1, 12))

    except ZeroDivisionError as zero:
        print(f"\nErreur {zero}")

    except TypeError as tyerr:
        print(f"\nErreur : {tyerr}")

    except ValueError as vaerr:
        print(f"\nErreur : {vaerr}")






    try:
        point1 = Point(2, 3)
        print(f"\nPoint créé : ({point1.x}, {point1.y})")

        point1.x = "Bonjour"

    except TypeError as terr:
        print(f"\nErreur : {terr}")

    except ValueError as verr:
        print(f"\nErreur : {verr}")

    finally:
        print("\nFin du test")
















import math


class Point:

    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y # __ = privé en python

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x:float):
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        return self.__y

    def __str__(self):
        return f"Point {self.__x},{self.__y}"

    def distanceCoord(self, a: float, b: float) -> float:
        return math.sqrt(math.pow(self.__x - a, 2) + math.pow(self.__y - b, 2))

    def distancePoint(self, camarade: Point) -> float:
        return self.distanceCoord(camarade.__x, camarade.__y)


class Cercle:

    def __init__(self, rayon: float, centre: Point = None):
        if centre is None:
            self.__centre = Point()
        else:
            self.__centre = centre

        self.rayon = rayon

    def __str__(self):
        return f"Cercle : centre = {self.__centre}, rayon = {self.__rayon}"

    @property
    def rayon(self) -> float:
        return self.__rayon

    @rayon.setter
    def rayon(self, valeur: float):
        if valeur < 0:
            raise ValueError("Un rayon ne peut pas être négatif !")
        self.__rayon = valeur

    def diametre(self) -> float:
        return 2 * self.__rayon

    def perimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        return math.pi * math.pow(self.__rayon, 2)

    def intersection(self, camarade: Cercle) -> bool:
        distance = self.__centre.distancePoint(camarade.__centre)

        return distance <= self.__rayon + camarade.__rayon

    def contientPoint(self, point: Point) -> bool:
        distance = self.__centre.distancePoint(point)

        return distance <= self.__rayon


class Rectangle:

    def __init__(self, point: Point = None, longueur: float = 1, hauteur: float = 1, pointHautDroit: Point = None):

        if point is None:
            self.__pointBasGauche = Point()
            self.__longueur = longueur
            self.__hauteur = hauteur

        elif pointHautDroit is not None:
            self.__pointBasGauche = point
            self.__longueur = pointHautDroit.distanceCoord(0, 0) - point.distanceCoord(0, 0)
            self.__hauteur = 0

        else:
            self.__pointBasGauche = point
            self.__longueur = longueur
            self.__hauteur = hauteur

    def __str__(self):
        return f"Rectangle : bas gauche = {self.__pointBasGauche}, longueur = {self.__longueur}, hauteur = {self.__hauteur}"

    def surface(self) -> float:
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        return 2 * (self.__longueur + self.__hauteur)

    def pointBasGauche(self) -> Point:
        return self.__pointBasGauche

    def pointBasDroit(self) -> Point:
        return Point(
            self.__pointBasGauche._Point__x + self.__longueur,
            self.__pointBasGauche._Point__y
        )

    def pointHautGauche(self) -> Point:
        return Point(
            self.__pointBasGauche._Point__x,
            self.__pointBasGauche._Point__y + self.__hauteur
        )

    def pointHautDroit(self) -> Point:
        return Point(
            self.__pointBasGauche._Point__x + self.__longueur,
            self.__pointBasGauche._Point__y + self.__hauteur
        )

    def contientPoint(self, point: Point) -> bool:
        x = point._Point__x
        y = point._Point__y

        xMin = self.__pointBasGauche._Point__x
        yMin = self.__pointBasGauche._Point__y

        xMax = xMin + self.__longueur
        yMax = yMin + self.__hauteur

        return xMin <= x <= xMax and yMin <= y <= yMax


class TriangleRectangle:

    def __init__(self, coteA: float, coteB: float, angleDroit: Point = None):

        if angleDroit is None:
            self.__angleDroit = Point()
        else:
            self.__angleDroit = angleDroit

        self.__coteA = coteA
        self.__coteB = coteB

    def __str__(self):
        return f"Triangle rectangle : angle droit = {self.__angleDroit}, cote A = {self.__coteA}, cote B = {self.__coteB}"

    def hypotenuse(self) -> float:
        return math.sqrt(math.pow(self.__coteA, 2) + math.pow(self.__coteB, 2))

    def perimetre(self) -> float:
        return self.__coteA + self.__coteB + self.hypotenuse()

    def surface(self) -> float:
        return (self.__coteA * self.__coteB) / 2

    def estIsocele(self) -> bool:
        return self.__coteA == self.__coteB


def Principale():

    print("===== POINT =====")

    point1 = Point(0, 0)
    point2 = Point(3, 4)

    print(f"Point 1 : {point1}")
    print(f"Point 2 : {point2}")

    print(f"Distance entre Point 1 et les coordonnées (3, 4) : {point1.distanceCoord(3, 4)}")
    print(f"Distance entre Point 1 et Point 2 : {point1.distancePoint(point2)}")

    print("\n===== CERCLE =====")

    cercle1 = Cercle(5)
    cercle2 = Cercle(3, Point(4, 0))

    print(cercle1)
    print(cercle2)

    print(f"Diamètre du cercle 1 : {cercle1.diametre()}")
    print(f"Périmètre du cercle 1 : {cercle1.perimetre()}")
    print(f"Surface du cercle 1 : {cercle1.surface()}")

    print(f"Les deux cercles sont en intersection : {cercle1.intersection(cercle2)}")

    point3 = Point(2, 2)

    print(f"Le point {point3} appartient au cercle 1 : {cercle1.contientPoint(point3)}")


    print("\n===== RECTANGLE =====")

    rectangle1 = Rectangle()
    rectangle2 = Rectangle(Point(2, 3), 5, 4)

    print(rectangle1)
    print(rectangle2)

    print(f"Surface du rectangle 2 : {rectangle2.surface()}")
    print(f"Périmètre du rectangle 2 : {rectangle2.perimetre()}")

    print(f"Point bas gauche : {rectangle2.pointBasGauche()}")
    print(f"Point bas droit : {rectangle2.pointBasDroit()}")
    print(f"Point haut gauche : {rectangle2.pointHautGauche()}")
    print(f"Point haut droit : {rectangle2.pointHautDroit()}")

    point4 = Point(4, 5)

    print(f"Le point {point4} est dans le rectangle : {rectangle2.contientPoint(point4)}")


    print("\n===== TRIANGLE RECTANGLE =====")

    triangle1 = TriangleRectangle(3, 4)
    triangle2 = TriangleRectangle(5, 5, Point(2, 2))

    print(triangle1)
    print(triangle2)

    print(f"Hypoténuse du triangle 1 : {triangle1.hypotenuse()}")
    print(f"Périmètre du triangle 1 : {triangle1.perimetre()}")
    print(f"Surface du triangle 1 : {triangle1.surface()}")
    print(f"Le triangle 1 est isocèle : {triangle1.estIsocele()}")

    print(f"Hypoténuse du triangle 2 : {triangle2.hypotenuse()}")
    print(f"Le triangle 2 est isocèle : {triangle2.estIsocele()}")


if __name__ == "__main__":
    Principale()

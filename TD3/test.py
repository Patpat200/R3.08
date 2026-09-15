import pytest
import math
from Exo1 import Point, Cercle

def test_defaut():
    p = Point()
    assert p.x == 0
    assert p.y == 0

def test_valeur():
    p = Point(2, 3)
    assert p.x == 2
    assert p.y == 3

def test_distance():
    p1 = Point(0, 0)
    assert p1.distanceCoord(3, 4) == 5.0

@pytest.mark.parametrize("x, y", [
    ("lettre", 5),
    (3, "texte"),
    ([1, 2], 3),
    (None, 0)
])


def test_point_type(x, y):
    with pytest.raises(TypeError):
        Point(x, y)


# CERCLE

def test_cercle():
    c = Cercle(5.0)
    assert c.rayon == 5.0
    assert c.centre.x == 0
    assert c.centre.y == 0

def test_cercle_centre():
    mon_centre = Point(10, 10)
    c = Cercle(3.5, mon_centre)
    assert c.rayon == 3.5
    assert c.centre.x == 10
    assert c.centre.y == 10

def test_cercle_negative():
    with pytest.raises(ValueError):
        Cercle(-10)

def test_cercle_type():
    with pytest.raises(TypeError):
        Cercle("dix")



def test_cercle_diametre():
    c = Cercle(5)
    assert c.diametre() == 10

def test_cercle_perimetre():
    c = Cercle(5)
    assert round(c.perimetre(), 2) == 31.42

def test_cercle_surface():
    c = Cercle(5)
    assert round(c.surface(), 2) == 78.54
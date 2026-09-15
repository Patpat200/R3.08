import pytest
from Exo1 import Point, Cercle


def test_distance():

    p1 = Point(0, 0)
    assert p1.distanceCoord(3, 4) == 5.0


def test_point():

    with pytest.raises(TypeError):
        erreur = Point("lettre", 5)

def test_cercle():

    with pytest.raises(ValueError):
        cercle = Cercle(-10)
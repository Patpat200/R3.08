
from Exo1 import Personnage, Guerrier, Mage, Joueur

def test_initialisation_personnage():
    perso = Personnage("Aventurier", 10)

    assert perso.pseudo == "Aventurier"
    assert perso.niveau == 10
    assert perso.pv == 10
    assert perso.initiative == 10


def test_stats_guerrier():
    guerrier = Guerrier("Conan", 5)

    assert guerrier.pv == 44

    assert guerrier.initiative == 26

    assert guerrier.degat() == 10


def test_stats_mage_et_mana():
    mage = Mage("Gandalf", 5)

    assert mage.pv == 35
    assert mage.degat() == 15

    for _ in range(6):
        mage.degat()

    assert mage.degat() == 5


def test_soin_limite():
    guerrier = Guerrier("Garen", 5)

    guerrier.pv -= 10
    assert guerrier.pv == 34

    guerrier.soigner()
    assert guerrier.pv == 39

    guerrier.soigner()
    guerrier.soigner()
    assert guerrier.pv == 44


def test_gestion_joueur():
    joueur = Joueur("Greg", 2)
    p1 = Personnage("Perso1")
    p2 = Personnage("Perso2")
    p3 = Personnage("Perso3")

    joueur.ajout_perso(p1)
    joueur.ajout_perso(p2)
    assert len(joueur.personnages) == 2

    joueur.ajout_perso(p3)
    assert len(joueur.personnages) == 2

    joueur.eliminer_personnage_pseudo("Perso1")
    assert len(joueur.personnages) == 1
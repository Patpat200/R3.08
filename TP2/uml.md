# Diagrammes de Classes UML - TP2 MMORPG

### Personnage
| **Personnage** |
|---|
| **- pseudo : str**<br>**- niveau : int**<br>**- pv : int**<br>**- initiative : int** |
| **+ Personnage(pseudo : str)**<br>**+ Personnage(pseudo : str, niveau : int)**<br>**+ attaque(autre : Personnage)**<br>**+ combat(autre : Personnage)**<br>**+ soigner()**<br>**+ degats() : int**<br>**+ \_\_eq\_\_(autre : Personnage) : bool** |

---

### Guerrier
| **Guerrier** |
|---|
| *(hérite de Personnage)* |
| **+ Guerrier(pseudo : str)**<br>**+ Guerrier(pseudo : str, niveau : int)**<br>**+ degats() : int** |

---

### Mage
| **Mage** |
|---|
| **- mana : int** |
| **+ Mage(pseudo : str)**<br>**+ Mage(pseudo : str, niveau : int)**<br>**+ degats() : int** |

---

### Joueur
| **Joueur** |
|---|
| **- nom : str**<br>**- max_personnages : int**<br>**- personnages : list** |
| **+ Joueur(nom : str, max_personnages : int)**<br>**+ ajouter_personnage(p : Personnage)**<br>**+ get_personnage(numero : int) : Personnage**<br>**+ get_personnage(pseudo : str) : Personnage**<br>**+ get_personnage(p : Personnage) : Personnage**<br>**+ eliminer_personnage(numero : int)**<br>**+ eliminer_personnage(pseudo : str)**<br>**+ eliminer_personnage(p : Personnage)** |
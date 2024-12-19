"""Module Plateau

Classes:
    * Plateau - Classe principale du plateau de jeu Quixo.
"""

from copy import deepcopy

from quixo_error import QuixoError


class Plateau:
    def __init__(self, plateau=None):
        """Constructeur de la classe Plateau

        Vous ne devez rien modifier dans cette méthode.

        Args:
            plateau (list[list[str]], optional): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None par défaut.
        """
        self.plateau = self.générer_le_plateau(deepcopy(plateau))

    def état_plateau(self):
        """Retourne une copie du plateau

        Retourne une copie du plateau pour éviter les effets de bord.
        Vous ne devez rien modifier dans cette méthode.

        Returns:
            list[list[str]]: La représentation du plateau
            tel que retourné par le serveur de jeu.
        """
        return deepcopy(self.plateau)

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du plateau

        Déplacer le code de votre fonction formater_plateau ici et ajuster le en conséquence.

        Returns:
            str: Une représentation en chaîne de caractères du plateau.
        """
        
        self.plateau = ""
        self.plateau += "   -------------------\n"  # Ligne de séparation de début
        longueur = len(self.plateau)
        for i in range(longueur):
            self.plateau += f"{i + 1} | {' | '.join(self.plateau[i])} |\n"
            if i < 4:
                self.plateau += "  |---|---|---|---|---|\n"
        self.plateau += "--|---|---|---|---|---|\n"  # Ligne de séparation finale ajustée
        self.plateau += "  | 1   2   3   4   5 |\n"  # Numéros de colonne encadrés
        return self.plateau

    def __getitem__(self, position):
        """Retourne la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du cube sur le plateau.

        Returns:
            str: La valeur à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
        """

        QuixoError().position_non_valide(position)
        return self.plateau[position[1] - 1][position[0] - 1]

    def __setitem__(self, position, valeur):
        """Modifie la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du cube sur le plateau.
            value (str): La valeur à insérer à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: Valeur du cube invalide.
        """
        QuixoError().valeur_invalide(valeur)
        QuixoError().position_non_valide(position)

        self.plateau[position[1] - 1][position[0] - 1] = valeur


    def générer_le_plateau(self, plateau):
        """Génère un plateau de jeu

        Si un plateau est fourni, il est retourné tel quel.
        Sinon, si la valeur est None, un plateau vide de 5x5 est retourné.

        Args:
            plateau (list[list[str]] | None): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None.

        Returns:
            list[list[str]]: La représentation du plateau
                tel que retourné par le serveur de jeu.

        Raises:
            QuixoError: Format du plateau invalide.
            QuixoError: Valeur du cube invalide.
        """
        if plateau is None:

            return [[' ']*5]*5
        QuixoError().taille_du_plateau_invalide(plateau)
        QuixoError().element_du_plateau_invalide(plateau)
        return plateau

    def insérer_un_cube(self, cube, origine, direction):
        """Insère un cube dans le plateau

        Cette méthode appelle la méthode d'insertion appropriée selon la direction donnée.

        À noter que la validation des positions sont faites dans
        les méthodes __setitem__ et __getitem__. Vous devez donc en faire usage dans
        les diverses méthodes d'insertion pour vous assurez que les positions sont valides.

        Args:
            cube (str): La valeur du cube à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du cube à insérer.
            direction (str): La direction de l'insertion, soit "haut", "bas", "gauche" ou "droite".

        Raises:
            QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".
            QuixoError: Le cube à insérer ne peut pas être vide.
        """

        QuixoError().pion_invalide(cube)
        QuixoError().direction_invalide(direction)
        if direction == 'haut':
            self.insérer_par_le_haut(cube, origine)
        if direction == 'bas':
            self.insérer_par_le_bas(cube, origine)
        if direction == 'gauche':
            self.insérer_par_la_gauche(cube, origine)
        if direction == 'droite':
            self.insérer_par_la_droite(cube, origine)

    def insérer_par_le_bas(self, cube, origine):
        """Insère un cube dans le plateau en direction du bas

        Args:
            cube (str): La valeur du cube à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du cube à insérer.
        """

        for i in range(origine[1], 5):
            self[origine[0], i] = self[origine[0], i + 1]
        self[origine[0], 5] = cube


    def insérer_par_le_haut(self, cube, origine):
        """Insère un cube dans le plateau en direction du haut

        Args:
            cube (str): La valeur du cube à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du cube à insérer.
        """

        for i in range(origine[1], 1, -1):
            self[origine[0], i] = self[origine[0], i - 1]
        self[origine[0], 1] = cube

    def insérer_par_la_gauche(self, cube, origine):
        """Insère un cube dans le plateau en direction de la gauche

        Args:
            cube (str): La valeur du cube à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du cube à insérer.
        """

        for i in range(origine[0], 1, -1):
            self[i, origine[1]] = self[i - 1, origine[1]]
        self[1, origine[1]] = cube

    def insérer_par_la_droite(self, cube, origine):
        """Insère un cube dans le plateau en direction de la droite

        Args:
            cube (str): La valeur du cube à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du cube à insérer.
        """

        for i in range(origine[0], 5):
            self[i, origine[1]] = self[i + 1, origine[1]]
        self[5, origine[1]] = cube
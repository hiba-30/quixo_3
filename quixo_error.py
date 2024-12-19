class QuixoError(Exception):
    
    def taille_du_plateau_invalide(self, plateau):
        for i in plateau:
            a = len(i) * len(plateau)
            if a != 25:
                raise QuixoError('Le plateau doit être une liste de 5 listes de 5 éléments')

    def element_du_plateau_invalide(self, plateau):
        for i in plateau:
            for j in i:
                if j not in ('X', 'O', ' '):
                    raise QuixoError('Les éléments du plateau doivent être "X", "O" ou " ".')

    def position_non_valide(self, position):
        if  position[0] > 5 and position[0] < 1 < position[1] > 5 and position[1] <1:
            raise QuixoError('Les positions x et y doivent être entre 1 et 5 inclusivement.')

    def valeur_invalide(self, valeur):
        if valeur not in ('X', 'O', ' '):
            raise QuixoError('La valeur donnée doit être "X", "O" ou " ".')

    def pion_invalide(self, pion):
        if pion not in ('X', 'O'):
            raise QuixoError('Le pion à insérer doit être "X" ou "O".')

    def direction_invalide(self, direction):
        if direction not in ('haut', 'bas', 'gauche', 'droite'):
            raise QuixoError('La direction doit être "haut", "bas", "gauche" ou "droite".')

    def nombre_de_pion_invalide(self, nb_pion):
        if nb_pion < 3 or nb_pion > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
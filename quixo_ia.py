from quixo import Quixo
from quixo_error import QuixoError
import random

class QuixoIA(Quixo):
    def lister_les_coups_possibles(self, plateau, cube):
        if cube not in ("X", "O"):
            raise QuixoError('Le cube doit être "X" ou "O".')
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")
        
        coups_possibles = []
        for i in range(1, 6):
            for j in range(1, 6):
                if plateau[i, j] == cube or plateau[i, j] == ' ':
                    if i == 1 and j != 1:
                        coups_possibles.append({"origine": [i, j], "direction": "droite"})
                        if j > 1:
                            coups_possibles.append({"origine": [i, j], "direction": "haut"})
                        if j < 5:
                            coups_possibles.append({"origine": [i, j], "direction": "bas"})
                    if i == 5 and j != 5:
                        coups_possibles.append({"origine": [i, j], "direction": "gauche"})
                        if j > 1:
                            coups_possibles.append({"origine": [i, j], "direction": "haut"})
                        if j < 5:
                            coups_possibles.append({"origine": [i, j], "direction": "bas"})
                    if j == 1 and i != 5:
                        coups_possibles.append({"origine": [i, j], "direction": "bas"})
                        if i > 1:
                            coups_possibles.append({"origine": [i, j], "direction": "gauche"})
                        if i < 5:
                            coups_possibles.append({"origine": [i, j], "direction": "droite"})
                    if j == 5 and i != 1:
                        coups_possibles.append({"origine": [i, j], "direction": "haut"})
                        if i > 1:
                            coups_possibles.append({"origine": [i, j], "direction": "gauche"})
                        if i < 5:
                            coups_possibles.append({"origine": [i, j], "direction": "droite"})
        return coups_possibles

    def analyser_le_plateau(self, plateau):
        analyseplateau = {
            "X": {2: 0, 3: 0, 4: 0, 5: 0},
            "O": {2: 0, 3: 0, 4: 0, 5: 0}
        }
        for joueur in ("X", "O"):
            for longueur in range(2, 6):
                analyseplateau[joueur][longueur] = plateau.compter_lignes(joueur, longueur)
        return analyseplateau

    def partie_terminée(self):
        if self.plateau.compter_lignes("X", 5) > 0:
            return "X"
        if self.plateau.compter_lignes("O", 5) > 0:
            return "O"
        return None
    
    def trouver_un_coup_vainqueur(self, joueur):
        coups_possibles = self.lister_les_coups_possibles(self.plateau, joueur)
        for coup in coups_possibles:
            plateau_simulé = self.plateau.simuler_coup(joueur, coup['origine'], coup['direction'])
            if plateau_simulé.partie_terminée() == joueur:
                return coup
        return None

    def trouver_un_coup_bloquant(self, joueur):
        adversaire = "O" if joueur == "X" else "X"
        coup_gagnant_adversaire = self.trouver_un_coup_vainqueur(adversaire)
        if coup_gagnant_adversaire:
            if coup_gagnant_adversaire in self.lister_les_coups_possibles(self.plateau, joueur):
                return coup_gagnant_adversaire
        return None
    
    def jouer_un_coup(self, joueur):
        if joueur not in ("X", "O"):
            raise QuixoError('Le symbole doit être "X" ou "O".')
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")

        coup_vain = self.trouver_un_coup_vain(joueur)
        if coup_vain:
            self.plateau.insérer_un_cube(joueur, coup_vain['origine'], coup_vain['direction'])
            return coup_vain

        coup_bloc = self.trouver_un_coup_bloc(joueur)
        if coup_bloc:
            self.plateau.insérer_un_cube(joueur, coup_bloc['origine'], coup_bloc['direction'])
            return coup_bloc

        coups_possibles = self.lister_les_coups_possibles(self.plateau, joueur)
        coup = random.choice(coups_possibles)
        self.plateau.insérer_un_cube(joueur, coup['origine'], coup['direction'])
        return coup

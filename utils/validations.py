"""
    Fonctions de validations : valider_nom, valider_prenom, valider_telephone et valider_email
"""
import re

def valider_chaine_caractere(chaine_caractere: str, taille_chaine_caractere: int=3) -> bool:
    """
        Fonction permettant de valider la chaîne de caractère :
        -> si la chaîne de caractère est vide
        -> vérifier la longueur minimale de la chaîne de caractère
        -> vérifier si la chaîne de caractère respecte la pattern regEx
    """
    chaine_caractere = chaine_caractere.strip()

    if not chaine_caractere:
        return False
    
    if len(chaine_caractere) < taille_chaine_caractere:
        return False
    
    regExChaineCaractere = r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$"
    return re.match(regExChaineCaractere, chaine_caractere) is not None

def valider_nom(nom: str) -> bool:
    """
        Fonction permettant de valider le nom
    """
    return valider_chaine_caractere(nom)
    

def valider_prenom(prenom: str) -> bool:
    """
        Fonction permettant de valider le prénom :
    """
    return valider_chaine_caractere(prenom)
    

def valider_telephone(telephone:str) -> bool:
    """
        Fonction permettant de valider le numéro de téléphone :
        -> si le numéro de téléphone est vide
        -> vérifier si le numéro de téléphone respecte la pattern regEx
    """   
    telephone = telephone.strip()

    if not telephone:
        return False
    
    regExTelephone = r"^\+?\d{8,15}$"
    return re.match(regExTelephone, telephone) is not None


def nettoyer_telephone(telephone: str) -> str:
    """
        Nettoyage : supprime tout sauf chiffres et +
    """
    return re.sub(r'[^\d+]', '', telephone.strip())


def valider_email(email:str) -> bool:
    """
        Fonction permettant de valider l'email' :
        -> si l'email' est vide
        -> vérifier si l'email' respecte la pattern regEx
    """   
    email = email.strip()

    if not email:
        return True
    
    regExEmail = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(regExEmail, email) is not None

    
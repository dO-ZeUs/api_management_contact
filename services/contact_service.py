"""
    FICHIER CONTENANT TOUTES 
    LES RÈGLES MÉTIER
"""

from database.contact_sql import creer_contact, modifier_contact, supprimer_contact, liste_contacts, rechercher_contact_telephone, rechercher_contact_id
from utils.validations import valider_nom, valider_prenom, valider_email, valider_telephone, nettoyer_telephone
from models.contact import Contact


def creer_nouveau_contact(nom, prenom, telephone, email):
    """
        Créer un nouveau contact après validation des données
    """
    # VALIDATION DES DONNEES
    if not valider_nom(nom):
        raise ValueError("Le nom est invalide, il doit contenir au moins 3 caractères et uniquement des lettres.")
    nom_final = nom

    if not valider_prenom(prenom):
        raise ValueError("Le nom est invalide, il doit contenir au moins 3 caractères etuniquement des lettres.")
    prenom_final = prenom

    if not valider_telephone(telephone):
        raise ValueError("Le téléphone est invalide, il doit contenir au moins 8 caractères et uniquement des chiffres.")
    telephone_final = nettoyer_telephone(telephone)
    
    if email.strip():
        if not valider_email(email):
            raise ValueError("Format de l'email est invalide, ex:toto@gmail.com")
        email_final = email.strip()
    else:
        email_final = None


    # VERIFIER L'UNICITE DU NUMERO DE TELEPHONE
    telephone_existant = rechercher_contact_telephone(telephone_final)
    if telephone_existant:
        raise ValueError("Ce numéro de téléphone existe déjà.")
    
    # CREER L'OBJET CONTACT
    nouveau_contact = Contact(
        id=None,
        nom=nom_final,
        prenom=prenom_final,
        telephone=telephone_final,
        email=email_final
    )
    return creer_contact(nouveau_contact)



def modifier_un_contact(id_contact, nom=None, prenom=None, telephone=None, email=None):
    """
        Modifier un contact existant
        Possibilité de modifier juste un champ et de conserver les anciennes données
    """
    if not isinstance(id_contact, int) or id_contact <= 0:
        raise ValueError("L'identifiant est invalide")
    
    contact_existant = rechercher_contact_id(id_contact)
    if not contact_existant:
        raise ValueError("Contact introuvable")
    
    nom_final = contact_existant.nom
    prenom_final = contact_existant.prenom
    telephone_final = contact_existant.telephone
    email_final = contact_existant.email

    if nom:
        if not valider_nom(nom):
            raise ValueError("Nom invalide")
        nom_final = nom.strip()

    if prenom:
        if not valider_prenom(prenom):
            raise ValueError("Prénom invalide")
        prenom_final = prenom.strip()

    if telephone:
        if not valider_telephone(telephone):
            raise ValueError("Téléphone invalide")
        telephone_nettoye = nettoyer_telephone(telephone)
        contact_tel = rechercher_contact_telephone(telephone_nettoye)
        if contact_tel and contact_tel.id != id_contact:
            raise ValueError("Ce numéro de téléphone est déjà utilisé par un autre contact")
        telephone_final = telephone_nettoye

    if email is not None:
        if email == "":
            email_final = None
        else:
            if valider_email(email):
                raise ValueError("Email invalide")
            email_final = email.strip()

    contact_modifier = Contact(
        id=id_contact,
        nom=nom_final,
        prenom=prenom_final,
        telephone=telephone_final,
        email=email_final
    )
    return modifier_contact(contact_modifier)



def supprimer_un_contact(id_contact):
    """
        Supprimer un contact
    """
    if not isinstance(id_contact, int) or id_contact <= 0:
        raise ValueError("L'identifiant est invalide")
    
    contact_existant = rechercher_contact_id(id_contact)
    if not contact_existant:
        raise ValueError("Le contact n'existe pas")
    return supprimer_contact(id_contact)



def liste_des_contacts():
    """
        Liste de tous les contacts dans la BD
    """
    return liste_contacts()



def rechercher_un_contact_id(id_contact):
    """
        Rechercher un contact via l'ID
    """
    if not isinstance(id_contact, int) or id_contact <= 0:
        raise ValueError("Identifiant invalide")
    
    contact_existant = rechercher_contact_id(id_contact)

    if not contact_existant:
        raise ValueError("Contact introuvable")
    return contact_existant



def rechercher_un_contact_telephone(telephone):
    """
        Rechercher un contact via 
        le numéro de téléphone
    """
    if not valider_telephone(telephone):
        raise ValueError("Numéro de téléphone invalide")
    telephone_final = nettoyer_telephone(telephone)
    contact_tel = rechercher_contact_telephone(telephone_final)
    if not contact_tel:
        raise ValueError("Aucun contact n'est lié à ce numéro !")
    return contact_tel




    


    

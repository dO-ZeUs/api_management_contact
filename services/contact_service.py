"""
    FICHIER CONTENANT TOUTES 
    LES RÈGLES MÉTIER
"""

from database.contact_sql import creer_contact, modifier_contact, supprimer_contact, liste_contacts, rechercher_contact_nom, rechercher_contact_telephone
from utils.validations import valider_nom, valider_prenom, valider_email, valider_telephone
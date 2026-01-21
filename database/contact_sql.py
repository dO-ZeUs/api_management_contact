"""
    Fichier contenant uniquement les
    requêtes SQL permettant de créer,
    modifier, supprimer, et lister les contacts
"""

import psycopg2
from psycopg2 import errors
from models.contact import Contact
from database.config_conn import se_connecter

def map_sql_contact(row):
    """
        PErmet de transformer une ligne
        de la BD en un objet(liste) Contact
    """
    return Contact(
        id_user = row[0],
        nom = row[1],
        prenom = row[2],
        telephone = row[3],
        email = row[4]
    )

def creer_contact(contact):
    """
        Insère un contact après création 
        dans la BD et retourne l'ID
    """
    try:
        # connexion à la BD 
        conn = se_connecter()
        cursor = conn.cursor()

        requete_creer_contatct = """
                        INSERT INTO contacts (nom, prenom, telephone, email)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id_user, nom, prenom, telephone, email;
                    """

        # exécuter la requête
        cursor.execute(
            requete_creer_contatct, (
                contact.nom,
                contact.prenom,
                contact.telephone,
                contact.email
            )
        )
        row = cursor.fetchone()
        # insérer la requête dans la BD : valider l'opération
        conn.commit()
        return map_sql_contact(row)
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        raise ValueError("Un ou plusieurs champs sont déjà utilisés par un autre contact.")
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur lors de la création du contact dans la BD: {e}")
    finally:
        cursor.close()
        conn.close()
            

def modifier_contact(contact):
    """
        Modifier un contact
    """
    try:
        conn = se_connecter()
        cursor = conn.cursor()

        requete_modifier_contact = """
                                        UPDATE contacts
                                        SET nom = %s, prenom = %s, telephone = %s, email = %s
                                        WHERE id_user = %s
                                        RETURNING id_user, nom, prenom, telephone, email;
                                """
        
        cursor.execute (
            requete_modifier_contact, (
                contact.nom,
                contact.prenom,
                contact.telephone,
                contact.email,
                contact.id_user
            )
        )

        row = cursor.fetchone()
        conn.commit()

        if row:
            return map_sql_contact(row)
        else: 
            raise ValueError("Aucun contact trouvé avec cet identifiant.")
        
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        raise ValueError("Un ou plusieurs champs sont déjà utilisés par un autre contact.")
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur lors de la modification du contact dans la BD: {e}")
    finally:
        cursor.close()
        conn.close()
        


def supprimer_contact(id_user):
    """
        Supprimer un contact
    """
    try:
        conn = se_connecter()
        cursor = conn.cursor()

        requete_supprimer_contact = """
                                        DELETE FROM contacts
                                        WHERE id_user = %s
                                        RETURNING id_user;
                                    """

        cursor.execute(
            requete_supprimer_contact, (id_user,)
        )
        row = cursor.fetchone()
        conn.commit()

        return row is not None
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur d'accès à la BD: {e}")
    finally:
        cursor.close()
        conn.close()


def liste_contacts():
    """
        Afficher la liste de 
        tous les contacts
    """
    try:
        conn = se_connecter()
        cursor = conn.cursor()

        requete_contacts = """
                                SELECT id_user, nom, prenom, telephone, email
                                FROM contacts;
                        """
        
        cursor.execute (requete_contacts)
        rows = cursor.fetchall()

        list_contact = []
        for row in rows:
            list_contact.append(map_sql_contact(row))
        return list_contact
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur d'accès à la BD: {e}")
    finally:
        cursor.close()
        conn.close()



def rechercher_contact_id(id_user):
    """
        Rechercher un contact
        via le nom
    """
    try:
        conn = se_connecter()
        cursor = conn.cursor()

        requete_contact_id = """
                                SELECT id_user, nom, prenom, telephone, email
                                FROM contacts
                                WHERE id_user = %s;
                            """
        
        cursor.execute (
            requete_contact_id, (id_user,)
        )

        row = cursor.fetchone()
        
        if row:
            return map_sql_contact(row)
        else:
            return None
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur d'accès à la BD: {e}")
    finally:
        cursor.close()
        conn.close()


def rechercher_contact_telephone(telephone):
    """
        Rechercher un contact
        via le numéro de téléphone
    """
    try:
        conn = se_connecter()
        cursor = conn.cursor()

        requete_contact_telephone = """
                                        SELECT id_user, nom, prenom, telephone, email
                                        FROM contacts
                                        WHERE telephone = %s;
                                    """
        
        cursor.execute (
            requete_contact_telephone, (telephone,)
        )

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return map_sql_contact(row)
        else:
            return None
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception("Erreur d'accès à la BD: {e}")
    finally:
        cursor.close()
        conn.close()
    
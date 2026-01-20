"""
    Fichier contenant uniquement les
    requêtes SQL permettant de créer,
    modifier, supprimer, et lister les contacts
"""

from models.contact import Contact
from config_conn import se_connecter

def map_sql_contact(row):
    """
        PErmet de transformer une ligne
        de la BD en un objet(liste) Contact
    """
    return Contact(
        id = row[0],
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
    
    # connexion à la BD 
    conn = se_connecter()
    cursor = conn.cursor()

    requete_creer_contatct = """
                    INSERT INTO contacts (nom, prenom, telephone, email)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, nom, prenom, telephone, email;
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

    # fermer le curseur et la connexion à la BD
    cursor.close()
    conn.close()

    return map_sql_contact(row)


def modifier_contact(contact):
    """
        Modifier un contact
    """
    conn = se_connecter()
    cursor = conn.cursor()

    requete_modifier_contact = """
                                    UPDATE contacts
                                    SET nom = %s, prenom = %s, telephone = %s, email = %s
                                    WHERE id = %s
                                    RETURNING id, nom, prenom, telephone, email;
                               """
    
    cursor.execute (
        requete_modifier_contact, (
            contact.nom,
            contact.prenom,
            contact.telephone,
            contact.email,
            contact.id
        )
    )

    row = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if row:
        return map_sql_contact(row)
    else: 
        return None


def supprimer_contact(id):
    """
        Supprimer un contact
    """

    conn = se_connecter()
    cursor = conn.cursor()

    requete_supprimer_contact = """
                                    DELETE FROM contacts
                                    WHERE id = %s
                                    RETURNING id;
                                """

    cursor.execute(
        requete_supprimer_contact, (id,)
    )
    row = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    return row is not None


def liste_contacts():
    """
        Afficher la liste de 
        tous les contacts
    """
    conn = se_connecter()
    cursor = conn.cursor()

    requete_contacts = """
                            SELECT id, nom, prenom, telephone, email
                            FROM contacts;
                       """
    
    cursor.execute (requete_contacts)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    list_contact = []
    for row in rows:
        list_contact.append(map_sql_contact(row))
    return list_contact


def rechercher_contact_nom(nom):
    """
        Rechercher un contact
        via le nom
    """
    conn = se_connecter()
    cursor = conn.cursor()

    requete_contact_nom = """
                            SELECT id, nom, prenom, telephone, email
                            FROM contacts
                            WHERE nom ILIKE %s;
                          """
    
    cursor.execute (
        requete_contact_nom, (f"%{nom}%",)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    list_contact_recherche_nom = []
    for row in rows:
        list_contact_recherche_nom.append(map_sql_contact(row))
    return list_contact_recherche_nom


def rechercher_contact_telephone(telephone):
    """
        Rechercher un contact
        via le numéro de téléphone
    """
    conn = se_connecter()
    cursor = conn.cursor()

    requete_contact_telephone = """
                                    SELECT id, nom, prenom, telephone, email
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
    
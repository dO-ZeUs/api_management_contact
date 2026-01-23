"""
    FONCTION PRINCIPALE DE L'API | GESTION DES CONTACTS
"""

from services.contact_service import creer_nouveau_contact, modifier_un_contact, supprimer_un_contact, liste_des_contacts, rechercher_un_contact_id, rechercher_un_contact_telephone


# Menu de l'app et choix de l'utilisateur
def choix_menu():
    print("================ Menu ================")
    print("1: Ajouter un contact")
    print("2: Modifier un contact")
    print("3: Supprimer un contact")
    print("4: Lister les contacts")
    print("5: Rechercher un contact")
    print("6: Quitter")
    print("-" *20)
    # l'utilisateur entre son choix
    choice = input("Votre choix: ").strip()
    return choice 


def afficher_contact(contact):
    print(f"ID: {contact.id}")
    print(f"Nom: {contact.nom}")
    print(f"Prénom: {contact.prenom}")
    print(f"Téléphone: {contact.telephone}")
    print(f"Email: {contact.email}")

def ajouter_contact():
    try:
        nom = input("Nom: ").upper().strip()
        prenom = input("Prénom: ").capitalize().strip()
        telephone = input("Numéro de téléphone: ").strip()
        email = input("Email(optionnel): ").strip()

        contact_cree = creer_nouveau_contact(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            email=email
        )

        print("Contact ajouté avec succès !")
        afficher_contact(contact_cree) 

    except  ValueError as e:
        print(f"Erreur: {e}.")
    except Exception as e:
        print(f"Erreur système: {e}")

    input("Appuyer sur Entrée pour revenir au menu...")


def modifier_contact():
    print("========== Modifier un contact ==========")
    try:
        afficher_liste_contacts()

        id_str = (input("ID du contact à modifier: "))
        if not id_str.isdigit():
            raise ValueError("L'identifiant doit être un nombre")
        
        id_contact = int(id_str)

        nom_modifier = input("Nouveau nom(laisser vide pour conserver): ").strip()
        prenom_modifier = input("Nouveau prénom(laisser vide pour conserver): ").strip()
        telephone_modifier = input("Nouveau numéro de téléphone(laisser vide pour conserver): ").strip()
        email_modifier = input("Nouvel email(optionnel)(laisser vide pour conserver): ").strip()

        contact_modifier = modifier_un_contact(
            id_contact=id_contact,
            nom=nom_modifier.upper() if nom_modifier else None,
            prenom=prenom_modifier.capitalize() if prenom_modifier else None,
            telephone=telephone_modifier if telephone_modifier else None,
            email=email_modifier if email_modifier else None
        )

        print("Contact modifié avec succès !")
        afficher_contact(contact_modifier)
    except  ValueError as e:
        print(f"Erreur: {e}.")
    except Exception as e:
        print(f"Erreur système: {e}")

    input("Appuyer sur Entrée pour revenir au menu...")


def supprimer_contact():
    print("========== Supprimer un contact ==========")
    try:
        afficher_liste_contacts()

        id_contact = int(input("ID du contact à supprimer: "))
        supprimer_un_contact(id_contact)

        print("Contact supprimé avec succès")
        liste_des_contacts()
    except  ValueError as e:
        print(f"Erreur: {e}.")
    except Exception as e:
        print(f"Erreur système: {e}")

    input("Appuyer sur Entrée pour revenir au menu...")


def afficher_liste_contacts():
    contacts = liste_des_contacts()

    if not contacts:
        print("Aucun contact enrégistré")
        return
    
    print("========== Liste des contacts ==========")
    for contact in contacts:
        afficher_contact(contact)
        print("-"*30)


def rechercher_un_contact():
    print("========== Rechercher un contact ==========")
    print("1: Par ID")
    print("2: Par numéro de téléphone")

    choix = input("Votre choix: ").strip()
    try:
        if choix == "1":
            liste_des_contacts()

            id_contact = int(input("ID du contact que vous recherchez: "))
            contact_id = rechercher_un_contact_id(id_contact)
            afficher_contact(contact_id)
        elif choix == "2":
            liste_des_contacts()
            telephone = input("Numéro de téléphone recherché: ")
            contact_tel = rechercher_un_contact_telephone(telephone)
            afficher_contact(contact_tel)
        else:
            print("Choix invalide")
    except  ValueError as e:
        print(f"Erreur: {e}.")
    except Exception as e:
        print(f"Erreur système: {e}")

    input("Appuyer sur Entrée pour revenir au menu...")

   
        

# Point d'entrée
if __name__ == "__main__":
    while True:
        user_choice = choix_menu()

        if user_choice == "1":
            ajouter_contact()
        elif user_choice == "2":
            modifier_contact()
        elif user_choice == "3":
            supprimer_contact()
        elif user_choice == "4":
            afficher_liste_contacts()
            input("Appuyer sur Entrée pour revenir au menu...")
        elif user_choice == "5":
            rechercher_un_contact()
        elif user_choice == "6":
            print("Bye !")
            break
        else:
            print("Choix invalide, veuillez rééssayer !")
 
      

            
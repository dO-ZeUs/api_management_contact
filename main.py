""" FONCTION PRINCIPALE DE L'APPLICATION """

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
    choice = input("Votre choix: ") 
    return choice 
        

# Point d'entrée
if __name__ == "__main__":
    while True:
        user_choice = choix_menu()

        if user_choice == "1":
            print("========== Ajouter un contact ==========")
        elif user_choice == "2":
            print("========== Modifier un contact ==========")
        elif user_choice == "3":
            print("========== Supprimer un contact ==========")
        elif user_choice == "4":
            print("========== Liste des contacts ==========")
        elif user_choice == "5":
            print("========== Rechercher un contact ==========")
        elif user_choice == "6":
            print("Bye !")
            break
        else:
            print("Choix invalide, veuillez rééssayer !")
 
      

            
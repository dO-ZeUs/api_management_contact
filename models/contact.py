""" DEFINIT LES DIFFERENTES DONNEES D'UN CONTACT """

class Contact:
    def __init__(self, id_user, nom, prenom, telephone, email):
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"ID: {self.id_user}, Nom: {self.nom}, Prénom: {self.prenom}, Téléphone: {self.telephone}, Email: {self.email}"
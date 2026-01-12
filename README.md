# Gestion de contacts – Backend Python (CLI)

## Description

Ce projet est une application backend développée en _Python natif_, connectée à une base de données _PostgreSQL_, permettant de gérer un carnet de contacts via une interface en ligne de commande (CLI).

L’objectif principal est de renforcer les _fondamentaux du développement backend_ sans framework, afin de mieux comprendre les mécanismes utilisés plus tard par des frameworks comme Django.

---

## Objectifs pédagogiques

-   Maîtriser Python côté backend sans framework
-   Comprendre et appliquer les opérations CRUD en SQL
-   Manipuler PostgreSQL depuis Python
-   Structurer un projet backend proprement
-   Gérer les erreurs et la validation des données
-   Séparer la logique métier de la logique technique

---

## Fonctionnalités

-   Ajouter un contact
-   Lister tous les contacts
-   Rechercher un contact (nom, prénom ou téléphone)
-   Modifier un contact existant
-   Supprimer un contact

---

## Règles de gestion

-   Le numéro de téléphone est **unique**
-   Les champs obligatoires doivent être renseignés
-   Les erreurs de saisie sont gérées proprement
-   Une confirmation est demandée avant suppression

---

## Modèle de données

Table `contacts` :

-   `id` : identifiant unique
-   `nom` : nom du contact
-   `prenom` : prénom du contact
-   `telephone` : numéro de téléphone (unique)
-   `email` : email (optionnel)
-   `created_at` : date de création

---

## Technologies utilisées

-   Python 3
-   PostgreSQL
-   psycopg / psycopg2
-   Interface en ligne de commande (CLI)

---

## Organisation du projet

Le projet est structuré de manière à séparer :

-   la connexion à la base de données
-   la logique métier
-   l’interface utilisateur (CLI)
-   les utilitaires (validation, affichage)

Cette organisation facilite la maintenance et prépare la transition vers Django.

---

## Lancement du projet

1. Créer la base de données PostgreSQL
2. Configurer les paramètres de connexion
3. Lancer l’application depuis le terminal
4. Utiliser le menu CLI pour gérer les contacts

---

## Bonnes pratiques appliquées

-   Code lisible et structuré
-   Gestion des exceptions
-   Validation des données en entrée
-   Utilisation des transactions SQL
-   Séparation des responsabilités

---

## Ce que ce projet démontre

Ce projet démontre ma capacité à :

-   développer un backend Python sans framework
-   concevoir une logique métier propre
-   travailler avec une base de données relationnelle
-   poser des bases solides avant l’utilisation de Django et Django REST Framework

---

## Perspectives

Ce projet constitue la base d’un parcours backend progressif.

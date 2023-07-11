# Réaliser un site de suivi de patients pour un psychologue


### About Dataset
Context

     I was looking for a well labeled dataset to perform a multiclass classification. I wanted to do something more than just sentiment classification, there is more than positive, negative and neutral sentiment in a sentence. I wanted to identify the emotion behind the words written. I found various txt files but it was a pain to clean and arrange the data again and again just to perform a simple classification. So I decided to prepare a csv file from all those text files and here you are, looking for text data just like me. All the best!
Content

     There are two columns, Text and Emotions. Quite self explanatory right. The Emotions column has various categories ranging from happiness to sadness to love and fear. Have fun building models which can identify what words denote what emotion. 

### Application de Suivi Psychologique
Cette application de suivi psychologique permet aux psychologues de gérer les données de leurs patients, d'analyser les émotions exprimées dans les journaux intimes des patients, et de fournir un suivi personnalisé.

#### Fonctionnalités
- Connexion sécurisée pour les psychologues et les patients.
- Visualisation de la répartition des émotions des patients actifs sur une période de temps donnée.
- Recherche des textes contenant des expressions spécifiques, filtrées par émotions et par nom/prénom du patient.
- Création de nouveaux patients avec un mot de passe par défaut, un nom et un prénom.
- Espace privé de connexion pour les patients.
- Création de nouveaux textes par les patients.
- Évaluation automatique des textes des patients à l'aide du modèle Hugging Face.

#### Installation
Clonez le dépôt GitHub :
git clone https://github.com/votre-utilisateur/app-suivi-psychologique.git


#### Technologies utilisées
- Python
- Django
- PostgreSQL (pour les données des patients et des psychologues)
     - Mettez à jour les packages existants en exécutant la commande suivante : sudo apt update
     - Installez PostgreSQL en utilisant la commande suivante :
 sudo apt install postgresql
     - Une fois l'installation terminée, PostgreSQL devrait être en cours d'exécution en arrière-plan. Vous pouvez vérifier son statut en utilisant la commande : sudo systemctl status postgresql
     - Vous pouvez également vérifier la version de PostgreSQL installée en utilisant la commande : psql --version
     Pour créer une nouvelle base de données PostgreSQL, suivez les étapes suivantes :
          - Connectez-vous à PostgreSQL en utilisant l'utilisateur postgres en exécutant la commande suivante : sudo -u postgres psql
          - Une fois connecté, vous serez dans l'interface de ligne de commande de PostgreSQL. Pour créer une nouvelle base de données, utilisez la commande suivante : CREATE DATABASE nom_de_la_base_de_donnees;
          - Vous pouvez vérifier que la base de données a bien été créée en utilisant la commande suivante : \l

- ElasticSearch (pour les textes et les évaluations)
Hugging Face (pour l'évaluation automatique des textes)

#### Auteurs
Rola EL-MOALLEM (@RolaMmss)
Noura Ousfia (@Noura-ou)

#### Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

